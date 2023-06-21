import pygame
from App_Carreras import AppJuegoDeCarreras
from Constantes import *
from Intro_Menu import IntroMenu
from Game_over import GameOverMenu
from Puntuaciones import Puntuaciones


pygame.init()

clock = pygame.time.Clock()
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
intro_menu = IntroMenu(pantalla)
juego_game = AppJuegoDeCarreras(pantalla)
punt_menu = Puntuaciones(pantalla)
game_over_menu = GameOverMenu(pantalla)
flag_correr = True

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
    
    if intro_menu.estado == "menu":
        intro_menu.dibujar_intro()
        intro_menu.procesar_eventos_menu(lista_eventos, intro_menu, juego_game)

    elif intro_menu.estado == "jugar":
        
        if juego_game.estado_juego == "jugando":
            juego_game.empezar_juego(lista_eventos)
        elif juego_game.estado_juego == "terminado":
            game_over_menu.dibujar_game_over()
            game_over_menu.procesar_eventos_game_over(lista_eventos, game_over_menu, intro_menu, juego_game)

    elif intro_menu.estado == "puntuaciones":
        punt_menu.dibujar_puntacion()
        punt_menu.procesar_eventos_puntuaciones(lista_eventos, punt_menu, intro_menu)
    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()


