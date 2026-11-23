from peewee import Model, MySQLDatabase

db = MySQLDatabase(
    "recetas_db",
    user="root",
    password="",
    host="localhost",
    port=3306,
    charset="utf8mb4",
)


class ModelBase(Model):
    class Meta:
        database = db


def abrir_conexion():
    if db.is_closed():
        db.connect()
    return db


def cerrar_conexion():
    if not db.is_closed():
        db.close()


class Conexion:
    def __init__(self):
        self.db = db

    def conectar(self):
        abrir_conexion()

    def cerrar(self):
        cerrar_conexion()