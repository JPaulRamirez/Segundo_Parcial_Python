import pygame
from Constantes import *
from Boton import Boton
from Cargar_imagen import CargarImagen

#------------------------------------------------------------------------------------------
#                   GAME OVER MENU
class GameOverMenu(CargarImagen):
    def __init__(self, pantalla):
        super().__init__(0, 0, ANCHO_VENTANA, ALTO_VENTANA, FONDO_GAME_OVER)
        self.pantalla = pantalla
        self.reiniciar_boton = Boton(pantalla, pygame.Rect(200, 800, 160, 50), "Reiniciar", COLOR_VINO, COLOR_NEGRO, TIPO_GRAFIA, 36)
        self.menu_boton = Boton(pantalla, pygame.Rect(10, 800, 140, 50), "Menu", COLOR_VINO, COLOR_NEGRO, TIPO_GRAFIA, 36)
        self.salir_boton = Boton(pantalla, pygame.Rect(650, 800, 140, 50), "Salir", COLOR_VINO, COLOR_NEGRO, TIPO_GRAFIA, 36)
        self.estado = "game_over"
        self.sonido_fin = pygame.mixer.Sound(SONIDO_GAMEOVER)
        self.sonido_fin.set_volume(0.3)
#------------------------------------------------------------------------------------------
    def procesar_eventos_game_over(self,eventos, game_over_menu, intro_menu, juego_game):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if game_over_menu.reiniciar_boton.colisiona_con_punto(evento.pos):
                    game_over_menu.estado = "reiniciar"
                    juego_game.reiniciar_juego()
                    juego_game.estado_juego = "jugando"
                elif game_over_menu.menu_boton.colisiona_con_punto(evento.pos):
                    game_over_menu.estado = "menu"
                    intro_menu.estado = "menu"
                    juego_game.estado_juego = "jugando"
                elif game_over_menu.salir_boton.colisiona_con_punto(evento.pos):
                    pygame.quit()
                    quit()
#------------------------------------------------------------------------------------------
    def dibujar_game_over(self):
        #self.pantalla.fill(COLOR_NEGRO)
        self.dibujar_imagen(self.pantalla,COLOR_NEGRO)
        self.reiniciar_boton.dibujar_boton()
        self.menu_boton.dibujar_boton()
        self.salir_boton.dibujar_boton()
#------------------------------------------------------------------------------------------

