import pygame
from Constantes import *
#---------------------------------------------------------------
#                   AUTO
class Auto:
    def __init__(self, x, y, ancho, alto, imagen):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.rect = self.imagen.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.hitbox = pygame.Rect(self.x , self.y, self.ancho - 15, self.alto - 10)
#---------------------------------------------------------------
    def dibujar_auto(self, pantalla):
        self.hitbox.x = self.rect.x + 8
        self.hitbox.y = self.rect.y + 5
        #pygame.draw.rect(pantalla, COLOR_CELESTE, self.hitbox)
        pantalla.blit(self.imagen, self.rect)
#---------------------------------------------------------------
    def establecer_posicion_inicial(self, x, y):
        self.rect.x = x
        self.rect.y = y
#---------------------------------------------------------------