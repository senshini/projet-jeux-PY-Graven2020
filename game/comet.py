import pygame
import random

# creer une classe pour gérer cette commet
class Comet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # definir l'image associée à cette comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1 ,3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("sol")
            #retirer la boule de feu