class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo


class Categoria:
    def __init__(self, id_categoria, nombre_categoria, descripcion):
        self.__id_categoria = id_categoria
        self.__nombre_categoria = nombre_categoria
        self.__descripcion = descripcion

    def get_id_categoria(self):
        return self.__id_categoria

    def get_nombre_categoria(self):
        return self.__nombre_categoria


class Receta:
    def __init__(self, id_receta, titulo, descripcion, tiempo_preparacion, dificultad, instrucciones, id_usuario, id_categoria):
        self.__id_receta = id_receta
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__tiempo_preparacion = tiempo_preparacion
        self.__dificultad = dificultad
        self.__instrucciones = instrucciones
        self.__id_usuario = id_usuario
        self.__id_categoria = id_categoria

    def get_id_receta(self):
        return self.__id_receta

    def get_titulo(self):
        return self.__titulo

    def get_instrucciones(self):
        return self.__instrucciones


class Ingredientes:
    def __init__(self, id_ingrediente, nombre_ingrediente, cantidad_medida):
        self.__id_ingrediente = id_ingrediente
        self.__nombre_ingrediente = nombre_ingrediente
        self.__cantidad_medida = cantidad_medida

    def get_nombre_ingrediente(self):
        return self.__nombre_ingrediente


class Valoracion:
    def __init__(self, id_valoracion, puntaje, comentario, fecha, id_receta, id_usuario):
        self.__id_valoracion = id_valoracion
        self.__puntaje = puntaje
        self.__comentario = comentario
        self.__fecha = fecha
        self.__id_receta = id_receta
        self.__id_usuario = id_usuario

    def get_puntaje(self):
        return self.__puntaje

