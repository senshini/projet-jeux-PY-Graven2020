import pygame
import math
from game import Game
pygame.init()

#gérer la fenetre de notre jeu
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080,720))

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

#importer notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)


#importer notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger notre jeu
game = Game()

running = True

#boucle tant que cette condition est vrai
while running:


    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #verifier si le jeu a commencer
    if game.is_playing:
        #déclencher le instructionde la partie
        game.update(screen)
    # vérifier si le jeu n'a pas commencer
    else:
        #ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


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


        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérification si la souris est en collision avec le bouton play
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()