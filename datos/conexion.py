import sqlite3
import os

class Conexion:
    def __init__(self):
        self.db_name = "recetas.db"

    def conectar(self):
        try:
            conexion = sqlite3.connect(self.db_name)
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
            return None