import pygame
import random
from Auto import *
from Constantes import *
#------------------------------------------------------------------------------------------
#                       ENEMIGOS
class Enemigo:
    def __init__(self, x, y, ancho, altura, imagenes_enemigos):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = altura
        self.imagenes_enemigos = imagenes_enemigos
        self.explosion_imagen = pygame.image.load(IMAGEN_BOOM)
        self.tiempo_genera_enemigo = TIEMPO_GENERAR_ELEMENTOS
        self.lista_enemigos = []
        self.sonido_explosion = pygame.mixer.Sound(SONIDO_EXPLOSION)
        self.sonido_explosion.set_volume(0.1)
#------------------------------------------------------------------------------------------
    def generar_enemigo(self, lista_enemigos):
        axu_nuevo_x = random.randrange(MIN, MAX, 100)
        if axu_nuevo_x != self.x:
            self.x = axu_nuevo_x
            enemigo = Auto(self.x, self.y, self.ancho, self.alto, random.choice(self.imagenes_enemigos))
            lista_enemigos.append(enemigo)
#------------------------------------------------------------------------------------------
    def generar_enemigos_periodicamente(self, generar_enemigo):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_genera_enemigo > generar_enemigo:
            self.tiempo_genera_enemigo = tiempo_actual
            self.generar_enemigo(self.lista_enemigos)
#------------------------------------------------------------------------------------------
    def mover_enemigos(self,velocidad_enemigo):
        for enemigo in self.lista_enemigos:
            enemigo.rect.y += velocidad_enemigo
#------------------------------------------------------------------------------------------
    def dibujar_enemigo(self,pantalla):
        for enemigo in self.lista_enemigos:
            enemigo.dibujar_auto(pantalla)
#------------------------------------------------------------------------------------------
    def colicion_enemigo(self,jugador,pantalla):
        for enemigo in self.lista_enemigos:
            if jugador.auto.hitbox.colliderect(enemigo.hitbox):
                jugador.perder_vida(1)
                self.sonido_explosion.play()
                self.lista_enemigos.remove(enemigo)
                self.dibujar_explosion(pantalla, enemigo.rect)

#------------------------------------------------------------------------------------------

    def dibujar_explosion(self, pantalla,rect):
        # Tamaño de la explosión igual al tamaño del rectángulo de colisión
        tamaño_explosion = (self.ancho, self.alto)  
        imagen_explosion_redimensionada = pygame.transform.scale(self.explosion_imagen, tamaño_explosion)
        pantalla.blit(imagen_explosion_redimensionada, (rect.x, rect.y))