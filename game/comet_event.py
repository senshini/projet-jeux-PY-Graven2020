import pygame

# crée une classe pour gérer cet evenement
class CometFallEvent:

    # lors du chargement -> créer un compteur
    def __init__(self):
        self.percent = 0
        self.percent_speed = 33

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def attempt_fall(self):
        # la jauge d'evenement est totalement chargé
        if self.is_full_loaded():
            print("Pluie de cometes !!")
            self.reset_percent()

    def update_bar(self, surface):

        # ajouter du pourcentage a la barre
        self.add_percent()

        # appel de la methode pour essayer de declencher la pluie de cometes
        self.attempt_fall()

        # barre noir (arriere)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des X
            surface.get_height() - 20, # l'axe des Y
            surface.get_width(), # longueur de la fenetre
            10 # epaisseur de la barre
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # l'axe des X
            surface.get_height() - 20, # l'axe des Y
            (surface.get_width() / 100) * self.percent, # longueur de la fenetre
            10 # epaisseur de la barre
        ])