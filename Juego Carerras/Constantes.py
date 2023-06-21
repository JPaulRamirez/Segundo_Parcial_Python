import os

# Directorio del juego
carpeta_juego = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_juego, "imagenes")
carpeta_sonidos = os.path.join(carpeta_juego, "sonidos")
# COLORES
COLOR_CELESTE = (0, 255, 255)
COLOR_AZUL_OSCURO = (11, 97, 194)
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_NEGRO = (0, 0, 0)
COLOR_VERDE = (0, 255, 0 )
COLOR_BLANCO = (255, 255, 255)
COLOR_VINO = (117, 0, 69)
COLOR_GRIS = (125, 125, 125)

# PANTALLA
ANCHO_VENTANA = 800 # X
ALTO_VENTANA = 1000 # Y
# SONIDO
SONIDO_PUNTOS = os.path.join(carpeta_sonidos,"puntos.wav")
SONIDO_BARRICADA = os.path.join(carpeta_sonidos,"choque.mp3")
SONIDO_EXPLOSION = os.path.join(carpeta_sonidos,"explocion.mp3")
SONIDO_MOTOR = os.path.join(carpeta_sonidos,"motor.mp3")
SONIDO_CLICK = os.path.join(carpeta_sonidos,"click.mp3")
SONIDO_GAMEOVER = os.path.join(carpeta_sonidos,"overArcade.mp3")
SONIDO_FONDO = os.path.join(carpeta_sonidos,"FondoMusic.mp3")
#TIPO GRAFIA
#Bodoni
TIPO_GRAFIA = "TipoGrafia\RacingGames-7B2rK.ttf"
# FPS
FPS = 60
# TIEMPO DE GENERAR ENEMIGOS
TIEMPO_GENERAR_ENEMIGO = 2500
TIEMPO_GENERAR_BONUS = 2200
TIEMPO_GENERAR_BARRICADA = 8000
TIEMPO_GENERAR_ELEMENTOS = 10000
#-------------------------------------------------------------------------------
# POSICION DEL JUGADOR
POSICION_X = 350
POSICION_Y = 850
# ALUTURA Y ANCHO DEL JUGADOR
ANCHO = 100
ALTURA = 160
# POSICION BONUS
POS_ENEMIGO_X = 150
POS_ENEMIGO_Y = -300
ANCHO_ENEMIGO = 100
ALTURA_ENEMIGO = 170
# POSICION BONUS
POS_BONUS_X = 0
POS_BONUS_Y = -300
ANCHO_BONUS = 50
ALTURA_BONUS = 50
# POSICION BARRICADA
POS_BARRICADA_X = 0
POS_BARRICADA_Y = -300
ANCHO_BARRICADA = 180
ALTURA_BARRICADA = 80
#-------------------------------------------------------------------------------
#VELOCIDAD DE MOVIMIENTO
VEL_ENEMIGO = 6
VEL_BONUS = 5
VEL_BARRICADA = 5
#-------------------------------------------------------------------------------
#IMAGEN DEL JUGADOR
IMAGEN_JUGADOR = os.path.join(carpeta_imagenes,"AutoRojo.png")   #Juego Carerras\Imagenes\AutoJugador.png"

# IMAGENES DE FONDO
FONDO_PISTA_CARRERA = os.path.join(carpeta_imagenes,"Pista2.png")
FONDO_INTRO_MENU = os.path.join(carpeta_imagenes,"FondoMenu2.png")
FONDO_GAME_OVER = os.path.join(carpeta_imagenes,"gameOver.png")
FONDO_PUNTUACIONES =os.path.join(carpeta_imagenes,"FondoPuntajes.png")

#IMAGENES BONUS
DICCIONARIO_PUNTOS_IMAGEN = {
    os.path.join(carpeta_imagenes,"Moneda.png"): 10,
    os.path.join(carpeta_imagenes,"Diamante.png"): 50,
    os.path.join(carpeta_imagenes,"aceite.png"): -35
}
#IMAGENES ENEMIGOS

LISTA_ENEMIGOS_IMAGEN= [
    os.path.join(carpeta_imagenes,"AutoAzul.png"),
    os.path.join(carpeta_imagenes,"Camion.png"),
    os.path.join(carpeta_imagenes,"Auto3.png"),
    os.path.join(carpeta_imagenes,"Camion2.png"),
    os.path.join(carpeta_imagenes,"Auto.png"),
    os.path.join(carpeta_imagenes,"Policia.png")
]

# IMAGENE EXPLOCION
IMAGEN_BOOM = os.path.join(carpeta_imagenes,"Boom.png")

# IMAGENE EXPLOCION
IMAGEN_BARRICADA = os.path.join(carpeta_imagenes,"Barricada.png")
#-------------------------------------------------------------------------------
# RANDOM
MIN = 150
MAX = 550