from auxiliares.seguridad import hashear_contrasena, verificar_contrasena
from datos.conexion import abrir_conexion, cerrar_conexion
from datos.modelos import Receta, Usuario
from datos.repositorio.receta_repo import (
    actualizar_receta_repo,
    buscar_recetas_repo,
    crear_receta_repo,
    eliminar_receta_repo,
    listar_recetas_repo,
)
from datos.repositorio.usuario_repo import (
    actualizar_usuario_repo,
    buscar_usuario_por_correo,
    crear_usuario_repo,
    eliminar_usuario_repo,
    listar_usuarios_repo,
)


def inicializar_sistema():
    db = abrir_conexion()
    db.create_tables([Usuario, Receta], safe=True)
    if not buscar_usuario_por_correo("admin@recetas.cl"):
        crear_usuario_repo(
            nombre="Administrador",
            correo="admin@recetas.cl",
            contrasena_hash=hashear_contrasena("Admin1234"),
            activo=1,
        )


def finalizar_sistema():
    cerrar_conexion()


def autenticar_usuario(correo: str, contrasena: str):
    usuario = buscar_usuario_por_correo(correo)
    if not usuario:
        return None
    if getattr(usuario, "activo", 1) != 1:
        return None
    if verificar_contrasena(contrasena, usuario.contrasena):
        return usuario
    return None


def crear_usuario(nombre: str, correo: str, contrasena: str):
    if not nombre.strip() or not correo.strip() or not contrasena.strip():
        return False, "Todos los campos son obligatorios."
    if buscar_usuario_por_correo(correo.strip()):
        return False, "Ya existe un usuario con ese correo."
    crear_usuario_repo(
        nombre=nombre.strip(),
        correo=correo.strip(),
        contrasena_hash=hashear_contrasena(contrasena),
        activo=1,
    )
    return True, "Usuario creado correctamente."


def obtener_usuarios():
    return listar_usuarios_repo()


def actualizar_usuario(uid: int, nombre: str, correo: str, activo: int):
    ok = actualizar_usuario_repo(
        uid=uid,
        nombre=nombre.strip() if nombre.strip() else None,
        correo=correo.strip() if correo.strip() else None,
        activo=activo,
    )
    if ok:
        return True, "Usuario actualizado."
    return False, "No se encontró el usuario."


def borrar_usuario(uid: int):
    if eliminar_usuario_repo(uid):
        return True, "Usuario eliminado."
    return False, "No se encontró el usuario."


def crear_receta(titulo: str, instrucciones: str, tiempo_preparacion: int, id_usuario: int):
    if not titulo.strip() or not instrucciones.strip():
        return False, "El título y las instrucciones son obligatorios."
    crear_receta_repo(
        titulo=titulo.strip(),
        instrucciones=instrucciones.strip(),
        tiempo_preparacion=tiempo_preparacion,
        id_usuario=id_usuario,
    )
    return True, "Receta creada correctamente."


def obtener_recetas():
    return listar_recetas_repo()


def buscar_recetas(termino: str):
    return buscar_recetas_repo(termino.strip())


def actualizar_receta(rid: int, titulo: str, instrucciones: str, tiempo_preparacion: int):
    ok = actualizar_receta_repo(
        rid=rid,
        titulo=titulo.strip() if titulo.strip() else None,
        instrucciones=instrucciones.strip() if instrucciones.strip() else None,
        tiempo_preparacion=tiempo_preparacion,
    )
    if ok:
        return True, "Receta actualizada."
    return False, "No se encontró la receta."


def borrar_receta(rid: int):
    if eliminar_receta_repo(rid):
        return True, "Receta eliminada."
    return False, "No se encontró la receta."