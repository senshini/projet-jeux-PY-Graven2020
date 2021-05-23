import pygame
import random

#crer une classe qui va gérer la notion de monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        #infliger les deagts
        self.health -= amount

        #vérifier si son nouveaux nombre de pts de vie est a 0
        if self.health <= 0:
            #Réapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

            # si la barre d'evenement est chargé à son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la methode pour essayer de d  eclencher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        #le déplacement ne se fait que si il n'y a pas de collision avec le gr de joueur
        if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity
        #si le monstre touche le joueur
        else:
            #infliger des dégats
            self.game.player.damage(self.attack)