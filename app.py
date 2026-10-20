from datos.conexion import Conexion
from datos.modelos import Usuario, Categoria, Receta, Ingredientes, Valoracion
from datos.repositorio import RepositorioRecetas

def inicializar_base_de_datos():
    conexion = Conexion()
    conn = conexion.conectar()
    if conn:
        with open("datos/sql/esquema.sql", "r", encoding="utf-8") as f:
            script_sql = f.read()
            conn.executescript(script_sql)
        conn.commit()
        conn.close()

def main():
    inicializar_base_de_datos()
    repo = RepositorioRecetas()

    while True:
        print("\n--- SISTEMA GESTIÓN DE RECETAS ---")
        print("1. Registrar Usuario")
        print("2. Ver Usuarios")
        print("3. Registrar Categoría")
        print("4. Ver Categorías")
        print("5. Registrar Receta")
        print("6. Ver Recetas (Detalladas)")
        print("7. Actualizar Receta")
        print("8. Eliminar Receta")
        print("9. Registrar Ingrediente")
        print("10. Ver Ingredientes")
        print("11. Registrar Valoración")
        print("12. Ver Valoraciones")
        print("13. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            usuario = Usuario(None, nombre, correo, contrasena)
            repo.guardar_usuario(usuario)
            print("¡Usuario registrado con éxito!")

        elif opcion == "2":
            print("\n--- LISTA DE USUARIOS ---")
            for u in repo.obtener_usuarios():
                print(f"ID: {u.get_id_usuario()} | Nombre: {u.get_nombre()} | Correo: {u.get_correo()}")

        elif opcion == "3":
            nombre_cat = input("Nombre de la categoría: ")
            desc_cat = input("Descripción: ")
            categoria = Categoria(None, nombre_cat, desc_cat)
            repo.guardar_categoria(categoria)
            print("¡Categoría registrada con éxito!")

        elif opcion == "4":
            print("\n--- LISTA DE CATEGORÍAS ---")
            for c in repo.obtener_categorias():
                print(f"ID: {c.get_id_categoria()} | Nombre: {c.get_nombre_categoria()}")

        elif opcion == "5":
            titulo = input("Título de la receta: ")
            descripcion = input("Descripción: ")
            
            try:
                tiempo = int(input("Tiempo de preparación (minutos): "))
            except ValueError:
                print("Error: Debes ingresar un número válido. Se asignará 0 por defecto.")
                tiempo = 0

            dificultad = input("Dificultad (Fácil, Media, Difícil): ")
            instrucciones = input("Instrucciones: ")
            
            try:
                id_usuario = int(input("ID del usuario creador: "))
                id_categoria = int(input("ID de la categoría: "))
            except ValueError:
                print("Error: Los IDs deben ser números enteros.")
                continue
            
            receta = Receta(None, titulo, descripcion, tiempo, dificultad, instrucciones, id_usuario, id_categoria)
            repo.guardar_receta(receta)
            print("¡Receta registrada con éxito!")

        elif opcion == "6":
            print("\n--- LISTA DETALLADA DE RECETAS ---")
            recetas_detalle = repo.obtener_recetas_detalladas()
            if not recetas_detalle:
                print("No hay recetas registradas todavía.")
            else:
                for r in recetas_detalle:
                    print(f"ID: {r[0]} | Título: {r[1]} | Descripción: {r[2]} | Tiempo: {r[3]} min | Dificultad: {r[4]} | Creador: {r[6]} | Categoría: {r[7]}")
                    print(f"Instrucciones: {r[5]}")
                    print("-" * 40)

        elif opcion == "7":
            try:
                id_receta = int(input("Ingresa el ID de la receta que quieres modificar: "))
            except ValueError:
                print("Error: El ID debe ser un número entero.")
                continue

            titulo = input("Nuevo título de la receta: ")
            descripcion = input("Nueva descripción: ")
            
            try:
                tiempo = int(input("Nuevo tiempo de preparación (minutos): "))
            except ValueError:
                tiempo = 0

            dificultad = input("Nueva dificultad (Fácil, Media, Difícil): ")
            instrucciones = input("Nuevas instrucciones: ")
            
            receta = Receta(id_receta, titulo, descripcion, tiempo, dificultad, instrucciones, None, None)
            repo.actualizar_receta(receta)
            print("¡Receta actualizada con éxito!")

        elif opcion == "8":
            try:
                id_receta = int(input("Ingresa el ID de la receta que quieres eliminar: "))
            except ValueError:
                print("Error: El ID debe ser numérico.")
                continue

            repo.eliminar_receta(id_receta)
            print("¡Receta eliminada correctamente!")

        elif opcion == "9":
            nombre_ing = input("Nombre del ingrediente: ")
            cantidad = input("Cantidad y medida (ej: 2 tazas): ")
            ingrediente = Ingredientes(None, nombre_ing, cantidad)
            repo.guardar_ingrediente(ingrediente)
            print("¡Ingrediente registrado con éxito!")

        elif opcion == "10":
            print("\n--- LISTA DE INGREDIENTES ---")
            for i in repo.obtener_ingredientes():
                print(f"Ingrediente: {i.get_nombre_ingrediente()}")

        elif opcion == "11":
            try:
                puntaje = int(input("Puntaje (1 al 5): "))
                id_receta = int(input("ID de la receta a valorar: "))
                id_usuario = int(input("ID del usuario que valora: "))
            except ValueError:
                print("Error: El puntaje y los IDs deben ser numéricos.")
                continue

            comentario = input("Comentario: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            
            valoracion = Valoracion(None, puntaje, comentario, fecha, id_receta, id_usuario)
            repo.guardar_valoracion(valoracion)
            print("¡Valoración guardada con éxito!")

        elif opcion == "12":
            print("\n--- LISTA DE VALORACIONES ---")
            for v in repo.obtener_valoraciones():
                print(f"Puntaje: {v.get_puntaje()} estrellas")

        elif opcion == "13":
            print("Saliendo del programa. ¡Mucho éxito en tu entrega!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()