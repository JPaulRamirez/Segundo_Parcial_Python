from Constantes import *
from Auto import *

#------------------------------------------------------------------------------------------
#                       JUGADOR
class Jugador: 
    def __init__(self,x,y,ancho,alto,imagen) -> None:
        self.auto = Auto(x,y,ancho,alto,imagen)
        self.vida = 5
        self.puntos = 0
        self.nombre_jugador = ""
        self.sonido_motor = pygame.mixer.Sound(SONIDO_MOTOR)
        self.sonido_motor.set_volume(0.3)
#------------------------------------------------------------------------------------------
    #Actualiza
    def mover (self):
        teclas = pygame.key.get_pressed()
        # Limite izquierdo
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            if self.auto.rect.x > 150:
                self.auto.rect.x -= 5
        
        # Limite derecho
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            if self.auto.rect.x < 550: 
                self.auto.rect.x += 5
        
        # Limite arriba
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            if self.auto.rect.y > 0:
                self.auto.rect.y -= 5
        
        # Limite abajo
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]: 
            if self.auto.rect.y < 850:
                self.auto.rect.y += 5
#------------------------------------------------------------------------------------------
    def dibujar(self, pantalla):
        self.auto.dibujar_auto(pantalla)
#------------------------------------------------------------------------------------------
    def establecer_posicion_inicial(self, x, y):
        self.auto.rect.x = x
        self.auto.rect.y = y
#------------------------------------------------------------------------------------------
    def perder_vida(self,daño):
        self.vida -= daño
#------------------------------------------------------------------------------------------        
    def sumar_puntos(self,puntos):
        self.puntos += puntos