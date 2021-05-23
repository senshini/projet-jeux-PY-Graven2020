import pygame
from game import Game
pygame.init()

#gérer la fenetre de notre jeu
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080,720))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

#charger notre jeu
game = Game()

running = True

#boucle tant que cette condition est vrai
while running:
    print(game.player.rect.x)
    print(game.player.health)
    print("jeu en marche")
    print(game.pressed.get(pygame.K_RIGHT))
    print(game.pressed.get(pygame.K_LEFT))

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    #actualiser la bar de vie
    game.player.update_health_bar(screen)

    #recuperer les projectilles du joueur
    for projectiles in game.player.all_projectiles:
        projectiles.move()

    #récup les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    #appliquer l'ensemble des images de mon groupede projectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l'ensemble des images de mon groupe de monstre
    game.all_monsters.draw(screen)

    #vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche aspace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
