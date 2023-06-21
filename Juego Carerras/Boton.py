import pygame
from Texto import Texto
from Constantes import *
#------------------------------------------------------------------------------------------
#                   BOTON
class Boton(Texto):
    def __init__(self, pantalla, rect, texto, color_relleno, color_texto, fuente, tamaño):
        super().__init__(pantalla, fuente, tamaño)
        self.rect = rect
        self.texto = texto
        self.color_relleno = color_relleno
        self.color_texto = color_texto
        self.sonido_click = pygame.mixer.Sound(SONIDO_CLICK)
        self.sonido_click.set_volume(0.3)
#------------------------------------------------------------------------------------------
    def dibujar_boton(self):
        pygame.draw.rect(self.pantalla, self.color_relleno, self.rect)
        centro_x = self.rect.centerx
        centro_y = self.rect.centery
        self.renderizar_texto(self.texto, self.color_texto, centro_x, centro_y)
#------------------------------------------------------------------------------------------
    def colisiona_con_punto(self, punto):
        self.sonido_click.play()
        return self.rect.collidepoint(punto)
#------------------------------------------------------------------------------------------