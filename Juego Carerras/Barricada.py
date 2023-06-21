import random
import pygame
from Constantes import *
from Cargar_imagen import CargarImagen
#------------------------------------------------------------------------------------------
#                   BARRICADA
class Barricada:
    def __init__(self, x, y, ancho, alto, imagen):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen_barricada = imagen
        self.tiempo_genera_barricada = TIEMPO_GENERAR_ELEMENTOS
        self.lista_barricadas = []
        self.sonido = pygame.mixer.Sound(SONIDO_BARRICADA)
        self.sonido.set_volume(0.1)
#------------------------------------------------------------------------------------------
    def generar_barricada(self):
        x = random.choice([140, 490])
        barricada = CargarImagen(self.x + x, self.y, self.ancho, self.alto, self.imagen_barricada)
        self.lista_barricadas.append(barricada)
#------------------------------------------------------------------------------------------
    def generar_barricada_periodicamente(self,generar_barricada):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_genera_barricada > generar_barricada: 
            self.tiempo_genera_barricada = tiempo_actual
            self.generar_barricada()
#------------------------------------------------------------------------------------------
    def mover_barricadas(self,velocidad_barricada):
        for barricada in self.lista_barricadas:
            barricada.rect.y += velocidad_barricada
#------------------------------------------------------------------------------------------
    def dibujar_barricadas(self, pantalla):
        for barricada in self.lista_barricadas:
            barricada.dibujar_imagen(pantalla,COLOR_NEGRO)     
#------------------------------------------------------------------------------------------
    def colicion_barricada(self,jugador):
        for barricada in self.lista_barricadas:
            if jugador.auto.hitbox.colliderect(barricada.hitbox):
                jugador.perder_vida(3)
                self.sonido.play()
                self.lista_barricadas.remove(barricada)
#------------------------------------------------------------------------------------------