from Constantes import *
from Cargar_imagen import CargarImagen

#------------------------------------------------------------------------------------------
#                   PISTA DE CARRERAS
class PistaCarreras(CargarImagen):
    def __init__(self, pantalla):
        super().__init__(0, 0, ANCHO_VENTANA, ALTO_VENTANA, FONDO_PISTA_CARRERA)
        self.pantalla = pantalla
        self.posicion_y = 0
#------------------------------------------------------------------------------------------
    def dibujar_pista(self):
        # Incrementa la posicion vertical
        self.posicion_y += 10
        if self.posicion_y >= ALTO_VENTANA:
            self.posicion_y = 0 #Renicia
        self.pantalla.blit(self.imagen, (0, self.posicion_y))
        self.pantalla.blit(self.imagen, (0, self.posicion_y - ALTO_VENTANA))
#------------------------------------------------------------------------------------------
    """    def dibujar_pista(self):
            altura_fondo = self.imagen.get_rect().height
            y_relativa = self.posicion_y % altura_fondo
            posicion_inicial = (0, y_relativa - altura_fondo)
            self.pantalla.blit(self.imagen, posicion_inicial)
            if y_relativa < ALTO_VENTANA:
                posicion_segunda = (0, y_relativa)
                self.pantalla.blit(self.imagen, posicion_segunda)
            self.posicion_y += 11"""
    

