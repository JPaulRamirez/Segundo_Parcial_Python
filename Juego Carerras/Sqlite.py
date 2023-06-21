import sqlite3
import json
#------------------------------------------------------------------------------------------
#                           SQLITE
class ConexionDB:
    def __init__(self):
        self.conexion = sqlite3.connect("puntuaciones.db")
        self.cursor = self.conexion.cursor()
        self.archivo_json = "puntuaciones.json"
        # Crea la tabla "puntajes" si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS puntajes
        (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, puntaje INTEGER)''')

#------------------------------------------------------------------------------------------
    def guardar_puntuacion(self, nombre, puntaje):
        try:
            self.cursor.execute("INSERT INTO puntajes (nombre, puntaje) VALUES (?, ?)", (nombre, puntaje))
            self.conexion.commit()
            print("Puntuacion guardada correctamente.")
        except:
            print("Error al guardar el puntaje:")
#------------------------------------------------------------------------------------------
    def generar_archivo_puntajes(self):
        try:
            self.cursor.execute("SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC")
            resultados = self.cursor.fetchall()
            # Crear diccionario de puntajes
            puntajes_dict = {"puntajes": []}
            for nombre, puntaje in resultados:
                puntajes_dict["puntajes"].append({"nombre": nombre, "puntos": puntaje})
            # Guardar como archivo JSON
            with open(self.archivo_json, "w") as archivo:
                json.dump(puntajes_dict, archivo, indent=4)
            print("Puntajes guardados con exito en el archivo JSON.")
        except:
            print("Error al guardar los puntajes como archivo JSON:")

#------------------------------------------------------------------------------------------






























    """def guardar_puntuacion(self, nombre, puntaje):
        try:
            # Guardar en la base de datos
            self.cursor.execute("INSERT INTO puntajes (nombre, puntaje) VALUES (?, ?)", (nombre, puntaje))
            self.conexion.commit()

            # Guardar en el archivo JSON
            with open(self.archivo_json, 'r') as file:
                data = json.load(file)
            
            # Agregar el nuevo registro al final de la lista
            nuevo_registro = {'nombre': nombre, 'puntaje': puntaje}
            data.append(nuevo_registro)

            # Guardar los registros actualizados en el archivo JSON
            with open(self.archivo_json, 'w') as file:
                json.dump(data, file)

            print("Puntuación guardada correctamente.")
        except sqlite3.Error as error:
            print("Error al guardar la puntuación:", error)
        except Exception as e:
            print("Error al guardar la puntuación en el archivo JSON:", str(e))

    def obtener_puntajes(self):
        self.cursor.execute("SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC")
        resultados = self.cursor.fetchall()
        return resultados
    
    def crear_archivo_json(self, archivo_json):
        try:
            with open(archivo_json, 'w') as file:
                json.dump([], file)
            print("Archivo JSON creado correctamente.")
        except Exception as e:
            print("Error al crear el archivo JSON:", str(e))
    
    def cargar_puntuaciones_desde_json(self):
        try:
            with open(self.archivo_json, 'r') as file:
                data = json.load(file)
                self.crear_archivo_json(self.archivo_json)  # Utiliza self.archivo_json aquí
                for record in data:
                    nombre = record['nombre']
                    puntaje = record['puntaje']
                    self.guardar_puntuacion(nombre, puntaje)
            print("Puntuaciones cargadas desde el archivo JSON correctamente.")
        except FileNotFoundError:
            print("El archivo JSON no existe.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")"""






"""    def guardar_puntuacion(self, nombre, puntaje):
        try:
            self.cursor.execute("INSERT INTO puntajes (nombre, puntaje) VALUES (?, ?)", (nombre, puntaje))
            self.conexion.commit()
            print("Puntuación guardada correctamente.")
        except sqlite3.Error as error:
            print("Error al guardar la puntuación:", error)"""