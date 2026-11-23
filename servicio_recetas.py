from datos.modelos import Receta
from datos.repositorio import RepositorioRecetas
from datos.auxiliares.validaciones import Validaciones

class ServicioRecetas:
    def __init__(self):
        self.repo = RepositorioRecetas()

    def crear_receta(self, titulo, descripcion, tiempo, dificultad, instrucciones, id_usuario=1, id_categoria=1):
        titulo_ok = Validaciones.validar_texto(titulo, "título")
        tiempo_ok = Validaciones.validar_entero_positivo(tiempo, "tiempo de preparación")
        dificultad_ok = Validaciones.validar_texto(dificultad, "dificultad")
        receta = Receta(None, titulo_ok, descripcion, tiempo_ok, dificultad_ok, instrucciones, id_usuario, id_categoria)
        self.repo.guardar_receta(receta)

    def listar_recetas(self):
        return self.repo.obtener_recetas_detalladas()

    def actualizar_receta(self, id_receta, titulo, descripcion, tiempo, dificultad, instrucciones):
        id_ok = Validaciones.validar_entero_positivo(id_receta, "ID de receta")
        titulo_ok = Validaciones.validar_texto(titulo, "título")
        tiempo_ok = Validaciones.validar_entero_positivo(tiempo, "tiempo de preparación")
        dificultad_ok = Validaciones.validar_texto(dificultad, "dificultad")
        receta = Receta(id_ok, titulo_ok, descripcion, tiempo_ok, dificultad_ok, instrucciones, 1, 1)
        self.repo.actualizar_receta(receta)

    def eliminar_receta(self, id_receta):
        id_ok = Validaciones.validar_entero_positivo(id_receta, "ID de receta")
        self.repo.eliminar_receta(id_ok)