import pygame
#------------------------------------------------------------------------------------------
#                       TEXTO
class Texto:
    def __init__(self, pantalla, fuente, tamaño):
        self.pantalla = pantalla
        self.fuente = fuente
        self.tamaño = tamaño
#------------------------------------------------------------------------------------------
    def renderizar_texto(self, texto, color, x, y):
        tipo_letra = pygame.font.Font(self.fuente, self.tamaño)
        superficie = tipo_letra.render(texto, True, color)
        rectangulo = superficie.get_rect(center=(x, y))
        self.pantalla.blit(superficie, rectangulo)
