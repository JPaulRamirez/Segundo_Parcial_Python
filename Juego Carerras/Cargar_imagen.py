import pygame
from Constantes import *

# ---------------------------------------------------------------
class CargarImagen:
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
        self.hitbox = pygame.Rect(self.x, self.y, self.ancho-25, self.alto)
#------------------------------------------------------------------------------------------
    def dibujar_imagen(self, pantalla,color):
        self.hitbox.x = self.rect.x+14
        self.hitbox.y = self.rect.y 
        #pygame.draw.rect(pantalla, color, self.hitbox) Mostar Hitbox
        pantalla.blit(self.imagen, self.rect)
#------------------------------------------------------------------------------------------