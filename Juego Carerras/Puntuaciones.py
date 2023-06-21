import pygame
import sqlite3
from Constantes import *
from Boton import *
from Texto import Texto
from Cargar_imagen import CargarImagen
#------------------------------------------------------------------------------------------
#                           PUNTUACIONES
class Puntuaciones(CargarImagen):
    def __init__(self, pantalla):
        super().__init__(0, 0, ANCHO_VENTANA, ALTO_VENTANA, FONDO_PUNTUACIONES)
        self.pantalla = pantalla
        self.menu_boton = Boton(pantalla, pygame.Rect(300, 740, 200, 50), "Menu", COLOR_GRIS, COLOR_NEGRO, TIPO_GRAFIA, 36)
        self.estado = "puntuaciones"
        self.texto = Texto(self.pantalla, TIPO_GRAFIA, 35)
#------------------------------------------------------------------------------------------    
    def procesar_eventos_puntuaciones(self,eventos, punt_menu, intro_menu):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if punt_menu.menu_boton.colisiona_con_punto(evento.pos):
                    punt_menu.estado = "menu"
                    intro_menu.estado = "menu"
#------------------------------------------------------------------------------------------    
    def dibujar_puntacion(self):
        self.dibujar_imagen(self.pantalla,COLOR_BLANCO)
        self.mostrar_puntuaciones()
        self.menu_boton.dibujar_boton()
#------------------------------------------------------------------------------------------    
    def mostrar_puntuaciones(self):
        try:
            conexion = sqlite3.connect("puntuaciones.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC LIMIT 10")#LIMIT 10
            puntuaciones = cursor.fetchall()
            conexion.close()         
            # Texto "Puntuaciones"
            self.texto.renderizar_texto("RANKING PUNTUACIONES", COLOR_VERDE, 390, 130)
            
            espacio_y = 50
            for nombre, puntaje in puntuaciones:
                # Texto de cada puntuación en la pantalla
                self.texto.renderizar_texto(f"{nombre}: {puntaje}",COLOR_VERDE, 400, 150 + espacio_y )
                espacio_y += 50
        except sqlite3.Error as error:
            print("Error al obtener las puntuaciones:", error)
#----------------------------------------------------------------------------------------------
    def mostrar_ingreso_nombre(self, nombre):
        # Reiniciar el valor del nombre a una cadena vacía
        nombre = ""  
        ingreso_completo = True
        while ingreso_completo:
            #teclas = pygame.key.get_pressed()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    quit()
                    #return
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                        ingreso_completo = False
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    elif len(nombre) <= 12:
                        nombre += evento.unicode
            #if teclas[pygame.K_BACKSPACE]:
            #    nombre = nombre[:-1]
            self.dibujar_imagen(self.pantalla,COLOR_BLANCO)
            
            # Dibuja el cuadro blanco
            pygame.draw.rect(self.pantalla, COLOR_NEGRO, pygame.Rect(110, 335, 290, 35))
            self.texto.renderizar_texto("Ingrese su nombre:", COLOR_VERDE, 250, 300)           
            # Lugar donde el usuario escribe
            self.texto.renderizar_texto(nombre, COLOR_VERDE, 260, 350)
            
            pygame.display.flip()
        return nombre
#------------------------------------------------------------------------------------------
