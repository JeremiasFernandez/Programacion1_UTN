import pygame
import const

class Character():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, const.alturaPersonaje, const.AnchoPersonaje)
        self.forma.center = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen,const.colorPersonaje, self.forma)
