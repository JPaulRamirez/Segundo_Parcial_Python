import pygame
from Constantes import *
from Bonus import Bonus
from Enemigo import Enemigo
from Jugador import Jugador
from Barricada import Barricada
from Puntuaciones import Puntuaciones
from Fondo_pista_carreras import PistaCarreras
from Texto import Texto
from Sqlite import ConexionDB
#---------------------------------------------------------------
#                  INICIAR JUEGO
#
class AppJuegoDeCarreras:
    def __init__(self, pantalla):
        self.estado_juego = "jugando"
        self.pantalla = pantalla
        #CLASES
        self.jugador = Jugador(POSICION_X, POSICION_Y, ANCHO, ALTURA,IMAGEN_JUGADOR)
        self.bonus = Bonus(POS_BONUS_X, POS_BONUS_Y, ANCHO_BONUS, ALTURA_BONUS, DICCIONARIO_PUNTOS_IMAGEN)
        self.barricada = Barricada(POS_BARRICADA_X, POS_BARRICADA_Y, ANCHO_BARRICADA, ALTURA_BARRICADA, IMAGEN_BARRICADA)
        self.enemigo = Enemigo(POS_ENEMIGO_X,POS_ENEMIGO_Y, ANCHO_ENEMIGO, ALTURA_ENEMIGO,LISTA_ENEMIGOS_IMAGEN)
        self.pista = PistaCarreras(pantalla)
        self.puntuaciones = Puntuaciones(pantalla)
        self.texto = Texto(self.pantalla, TIPO_GRAFIA, 25)
        #-------------------
        self.game_paused = True
        self.conexion_db = ConexionDB()

    def obtener_puntajes(self):
        self.conexion_db.generar_archivo_puntajes()

    def guardar_puntuacion(self, nombre, puntaje):
        self.conexion_db.guardar_puntuacion(nombre, puntaje)
    
    def game_over(self):
        if self.jugador.vida <= 0:
            self.jugador.nombre_jugador = self.puntuaciones.mostrar_ingreso_nombre(self.jugador.nombre_jugador)
            self.guardar_puntuacion(self.jugador.nombre_jugador, self.jugador.puntos)
            self.obtener_puntajes()
            self.estado_juego = "terminado"

    def verificar_colision(self):
        self.enemigo.colicion_enemigo(self.jugador,self.pantalla)
        self.bonus.colicion_bonus(self.jugador)
        self.barricada.colicion_barricada(self.jugador)
    
    def dibujar_elementos(self):
        self.enemigo.dibujar_enemigo(self.pantalla)
        self.bonus.dibujar_bonus(self.pantalla)
        self.barricada.dibujar_barricadas(self.pantalla)  


    def velocidades_de_posicion_vertical(self):
        # Actualiza la posición vertical de los elementos(update)
        self.enemigo.mover_enemigos(VEL_ENEMIGO)
        self.bonus.mover_bonus(VEL_BONUS)
        self.barricada.mover_barricadas(VEL_BARRICADA)


    def generar_elementos_periodicamente(self):
        self.enemigo.generar_enemigos_periodicamente(TIEMPO_GENERAR_ENEMIGO)
        self.bonus.generar_bonus_periodicamente(TIEMPO_GENERAR_BONUS)
        self.barricada.generar_barricada_periodicamente(TIEMPO_GENERAR_BARRICADA)
    
    def reiniciar_juego(self):
        self.estado_juego = "jugando"
        self.jugador.vida = 3
        self.jugador.puntos = 0
        self.enemigo.lista_enemigos.clear()
        self.barricada.lista_barricadas.clear()
        self.bonus.lista_bonus.clear()
        self.jugador.establecer_posicion_inicial(POSICION_X, POSICION_Y)

    def empezar_juego(self,eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_p:
                if self.game_paused == True:
                    self.game_paused = False
                else:
                    self.game_paused = True  
        if self.game_paused == True:
            if self.estado_juego == "jugando":
                self.jugador.mover()            
                self.generar_elementos_periodicamente()
                self.velocidades_de_posicion_vertical()
                self.pista.dibujar_pista()
                self.jugador.dibujar(self.pantalla) 
                self.dibujar_elementos()
                self.verificar_colision()
                self.game_over()
            if TIEMPO_GENERAR_ELEMENTOS > pygame.time.get_ticks():
                self.texto.renderizar_texto("CONTROLOES: W A D S", COLOR_NEGRO, 400, 300) # ↑ ← ↓ →
            self.texto.renderizar_texto(f"VIDA: {self.jugador.vida}", COLOR_ROJO, 50, 50)
            self.texto.renderizar_texto(f"PUNTOS: {self.jugador.puntos}", COLOR_AZUL, 75, 80)
        else:
            self.texto.renderizar_texto("PAUSE", COLOR_NEGRO, 450, 500)
