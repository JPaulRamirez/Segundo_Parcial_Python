import pygame
import random
from Constantes import *
from Cargar_imagen import CargarImagen
#------------------------------------------------------------------------------------------
#                                     BONUS
class Bonus:
    def __init__(self, x, y, ancho, alto, imagenes):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagenes_bonus = imagenes
        self.tiempo_genera_bonus = TIEMPO_GENERAR_ELEMENTOS
        self.lista_bonus = []
        self.sonido_bonus = pygame.mixer.Sound(SONIDO_PUNTOS)
        self.sonido_bonus.set_volume(0.2)
# ---------------------------------------------------------------
    def generar_bonus(self, lista_bonus): 
        # Genera la posicion X entre 150-550
        x = random.randrange(MIN, MAX, 50)
        imagen = random.choice(list(self.imagenes_bonus))
        #Optengo su valor del diccionario
        puntos = self.imagenes_bonus.get(imagen)
        bonus = CargarImagen(self.x + x, self.y, self.ancho, self.alto, imagen)
        bonus.puntos = puntos
        lista_bonus.append(bonus)

# ---------------------------------------------------------------    
    def generar_bonus_periodicamente(self,generar_bonus):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_genera_bonus > generar_bonus:
            self.tiempo_genera_bonus = tiempo_actual
            self.generar_bonus(self.lista_bonus)
# ---------------------------------------------------------------

    def colicion_bonus(self,jugador):
        for bonus in self.lista_bonus:
            if jugador.auto.hitbox.colliderect(bonus.hitbox):
                jugador.sumar_puntos(bonus.puntos)
                self.sonido_bonus.play()
                self.lista_bonus.remove(bonus)
# ---------------------------------------------------------------
    def mover_bonus(self,velocidad_bonus):
        for bonus in self.lista_bonus:
            bonus.rect.y += velocidad_bonus

# ---------------------------------------------------------------
    def dibujar_bonus(self,pantalla):
        #self.mover_bonus()
        for bonus in self.lista_bonus:
            bonus.dibujar_imagen(pantalla,COLOR_NEGRO)