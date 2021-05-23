from monster import Monster
from player import Player
from comet_event import CometFallEvent
import pygame

#creer une seconde class qui va represneter notre jeu
class Game:

    def __init__(self):
        #definir si le jeux a commencer
        self.is_playing = True
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent()
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self,):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remettre le jeu a neuf
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la bar de vie
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement
        self.comet_event.update_bar(screen)

        # recuperer les projectilles du joueur
        for projectiles in self.player.all_projectiles:
            projectiles.move()

        # récup les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images de mon groupede projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)