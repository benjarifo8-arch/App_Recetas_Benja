from datos.conexion import Conexion
from datos.modelos import Usuario, Categoria, Receta, Ingredientes, Valoracion

class RepositorioRecetas:
    def __init__(self):
        self.conexion = Conexion()

    def guardar_usuario(self, usuario):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, contrasena) VALUES (%s, %s, %s)",
                (usuario.get_nombre(), usuario.get_correo(), usuario._Usuario__contrasena)
            )
            conn.commit()
            conn.close()

    def obtener_usuarios(self):
        conn = self.conexion.conectar()
        usuarios = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario, nombre, correo, contrasena FROM usuarios")
            for fila in cursor.fetchall():
                usuarios.append(Usuario(fila[0], fila[1], fila[2], fila[3]))
            conn.close()
        return usuarios

    def guardar_categoria(self, categoria):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO categorias (nombre_categoria, descripcion) VALUES (%s, %s)",
                (categoria.get_nombre_categoria(), categoria._Categoria__descripcion)
            )
            conn.commit()
            conn.close()

    def obtener_categorias(self):
        conn = self.conexion.conectar()
        categorias = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_categoria, nombre_categoria, descripcion FROM categorias")
            for fila in cursor.fetchall():
                categorias.append(Categoria(fila[0], fila[1], fila[2]))
            conn.close()
        return categorias

    def guardar_receta(self, receta):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO recetas (titulo, descripcion, tiempo_preparacion, dificultad, instrucciones, id_usuario, id_categoria) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (receta.get_titulo(), receta._Receta__descripcion, receta._Receta__tiempo_preparacion, 
                 receta._Receta__dificultad, receta.get_instrucciones(), receta._Receta__id_usuario, receta._Receta__id_categoria)
            )
            conn.commit()
            conn.close()

    def obtener_recetas_detalladas(self):
        conn = self.conexion.conectar()
        recetas = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT r.id_receta, r.titulo, r.descripcion, r.tiempo_preparacion, r.dificultad, r.instrucciones, u.nombre, c.nombre_categoria 
                FROM recetas r
                JOIN usuarios u ON r.id_usuario = u.id_usuario
                JOIN categorias c ON r.id_categoria = c.id_categoria
            """)
            for fila in cursor.fetchall():
                recetas.append(fila)
            conn.close()
        return recetas

    def actualizar_receta(self, receta):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                """UPDATE recetas SET titulo = %s, descripcion = %s, tiempo_preparacion = %s, dificultad = %s, instrucciones = %s 
                   WHERE id_receta = %s""",
                (receta.get_titulo(), receta._Receta__descripcion, receta._Receta__tiempo_preparacion, 
                 receta._Receta__dificultad, receta.get_instrucciones(), receta.get_id_receta())
            )
            conn.commit()
            conn.close()

    def eliminar_receta(self, id_receta):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM recetas WHERE id_receta = %s", (id_receta,))
            conn.commit()
            conn.close()

    def guardar_ingrediente(self, ingrediente):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO ingredientes (nombre_ingrediente, cantidad_medida) VALUES (%s, %s)",
                (ingrediente.get_nombre_ingrediente(), ingrediente._Ingredientes__cantidad_medida)
            )
            conn.commit()
            conn.close()

    def obtener_ingredientes(self):
        conn = self.conexion.conectar()
        ingredientes = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_ingrediente, nombre_ingrediente, cantidad_medida FROM ingredientes")
            for fila in cursor.fetchall():
                ingredientes.append(Ingredientes(fila[0], fila[1], fila[2]))
            conn.close()
        return ingredientes

    def guardar_valoracion(self, valoracion):
        conn = self.conexion.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO valoraciones (puntaje, comentario, fecha, id_receta, id_usuario) VALUES (%s, %s, %s, %s, %s)",
                (valoracion.get_puntaje(), valoracion._Valoracion__comentario, valoracion._Valoracion__fecha, valoracion._Valoracion__id_receta, valoracion._Valoracion__id_usuario)
            )
            conn.commit()
            conn.close()

    def obtener_valoraciones(self):
        conn = self.conexion.conectar()
        valoraciones = []
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_valoracion, puntaje, comentario, fecha, id_receta, id_usuario FROM valoraciones")
            for fila in cursor.fetchall():
                valoraciones.append(Valoracion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
            conn.close()
        return valoraciones