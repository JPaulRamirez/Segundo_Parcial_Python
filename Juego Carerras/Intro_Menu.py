import pygame
from Constantes import *
from Boton import Boton
from Cargar_imagen import CargarImagen
#------------------------------------------------------------------------------------------
#                           MENU
class IntroMenu(CargarImagen):
    def __init__(self, pantalla):
        super().__init__(0, 0, ANCHO_VENTANA, ALTO_VENTANA,FONDO_INTRO_MENU)
        self.pantalla = pantalla
        self.empezar_boton = Boton(pantalla, pygame.Rect(300, 200, 200, 50), "Empezar", COLOR_AZUL_OSCURO, COLOR_NEGRO,TIPO_GRAFIA, 36)
        self.puntuaciones_boton = Boton(pantalla, pygame.Rect(300, 270, 200, 50), "Puntajes", COLOR_AZUL_OSCURO, COLOR_NEGRO, TIPO_GRAFIA, 36)
        self.salir_boton = Boton(pantalla, pygame.Rect(300, 340, 200, 50), "Salir", COLOR_AZUL_OSCURO, COLOR_NEGRO, TIPO_GRAFIA, 36)
        self.estado = "menu"
        #self.sonido_fondo = pygame.mixer.Sound(SONIDO_FONDO)
        #self.sonido_fondo.set_volume(0.3)
#------------------------------------------------------------------------------------------
    def procesar_eventos_menu(self, eventos, intro_menu, juego_game):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                #Si precione el click izquierdo  
                if evento.button == 1:
                    if intro_menu.empezar_boton.colisiona_con_punto(evento.pos):
                        intro_menu.estado = "jugar"
                        juego_game.reiniciar_juego()
                        juego_game.estado_juego = "jugando"
                    elif intro_menu.puntuaciones_boton.colisiona_con_punto(evento.pos):
                        intro_menu.estado = "puntuaciones"
                    elif intro_menu.salir_boton.colisiona_con_punto(evento.pos):
                        pygame.quit()
                        quit()
#------------------------------------------------------------------------------------------  
    def dibujar_intro(self):
        #self.pantalla.fill(COLOR_CELESTE)
        #self.sonido_fondo.play() 
        self.dibujar_imagen(self.pantalla,COLOR_NEGRO)
        self.empezar_boton.dibujar_boton()
        self.puntuaciones_boton.dibujar_boton()
        self.salir_boton.dibujar_boton()
#------------------------------------------------------------------------------------------
