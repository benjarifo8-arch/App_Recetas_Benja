from auxiliares.seguridad import solicitar_contrasena
from negocio.servicio_ev3 import (
    inicializar_sistema,
    finalizar_sistema,
    autenticar_usuario,
    crear_usuario,
    obtener_usuarios,
    actualizar_usuario,
    borrar_usuario,
    crear_receta,
    obtener_recetas,
    buscar_recetas,
    actualizar_receta,
    borrar_receta,
)


def login():
    print("\n=== INICIO DE SESIÓN ===")
    for intento in range(3):
        correo = input("Correo: ").strip()
        clave = solicitar_contrasena("Contraseña: ")
        usuario = autenticar_usuario(correo, clave)
        if usuario:
            print(f"Bienvenido/a, {usuario.nombre}.")
            return usuario
        print(f"Credenciales inválidas (intento {intento + 1}/3).")
    print("Se agotaron los intentos de inicio de sesión.")
    return None


def menu_usuarios():
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("0. Volver")
        op = input("Opción: ").strip()

        if op == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            clave = solicitar_contrasena("Contraseña: ")
            ok, msg = crear_usuario(nombre, correo, clave)
            print(msg)
        elif op == "2":
            for u in obtener_usuarios():
                estado = "Activo" if u.activo == 1 else "Inactivo"
                print(f"[{u.id_usuario}] {u.nombre} | {u.correo} | {estado}")
        elif op == "3":
            try:
                uid = int(input("ID usuario a modificar: "))
                nombre = input("Nuevo nombre (vacío para mantener): ")
                correo = input("Nuevo correo (vacío para mantener): ")
                activo = int(input("Estado (1=Activo, 0=Inactivo): "))
                ok, msg = actualizar_usuario(uid, nombre, correo, activo)
                print(msg)
            except ValueError:
                print("Ingresa un ID y estado numérico válido.")
        elif op == "4":
            try:
                uid = int(input("ID usuario a eliminar: "))
                ok, msg = borrar_usuario(uid)
                print(msg)
            except ValueError:
                print("Ingresa un ID válido.")
        elif op == "0":
            break
        else:
            print("Opción no válida.")


def menu_recetas(usuario_actual):
    while True:
        print("\n--- GESTIÓN DE RECETAS ---")
        print("1. Crear receta")
        print("2. Listar recetas")
        print("3. Buscar receta por título")
        print("4. Modificar receta")
        print("5. Eliminar receta")
        print("0. Volver")
        op = input("Opción: ").strip()

        if op == "1":
            titulo = input("Título: ")
            instrucciones = input("Instrucciones: ")
            try:
                tiempo = int(input("Tiempo de preparación (min): "))
            except ValueError:
                tiempo = 30
            ok, msg = crear_receta(titulo, instrucciones, tiempo, usuario_actual.id_usuario)
            print(msg)
        elif op == "2":
            for r in obtener_recetas():
                print(f"[{r.id_receta}] {r.titulo} ({r.tiempo_preparacion} min) - {r.instrucciones}")
        elif op == "3":
            termino = input("Buscar título: ")
            for r in buscar_recetas(termino):
                print(f"[{r.id_receta}] {r.titulo} ({r.tiempo_preparacion} min)")
        elif op == "4":
            try:
                rid = int(input("ID receta a modificar: "))
                titulo = input("Nuevo título (vacío para mantener): ")
                instrucciones = input("Nuevas instrucciones (vacío para mantener): ")
                tiempo = int(input("Nuevo tiempo (min): "))
                ok, msg = actualizar_receta(rid, titulo, instrucciones, tiempo)
                print(msg)
            except ValueError:
                print("Ingresa valores numéricos válidos.")
        elif op == "5":
            try:
                rid = int(input("ID receta a eliminar: "))
                ok, msg = borrar_receta(rid)
                print(msg)
            except ValueError:
                print("Ingresa un ID válido.")
        elif op == "0":
            break
        else:
            print("Opción no válida.")


def ejecutar_app_ev3():
    inicializar_sistema()
    try:
        usuario = login()
        if not usuario:
            return
        while True:
            print("\n=== MENÚ PRINCIPAL (EVALUACIÓN N°3) ===")
            print("1. Gestión de Usuarios (CRUD)")
            print("2. Gestión de Recetas (CRUD)")
            print("0. Salir")
            op = input("Opción: ").strip()
            if op == "1":
                menu_usuarios()
            elif op == "2":
                menu_recetas(usuario)
            elif op == "0":
                print("Cerrando sesión...")
                break
            else:
                print("Opción no válida.")
    finally:
        finalizar_sistema()