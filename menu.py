from negocio.servicio_recetas import ServicioRecetas


def iniciar_menu():
  servicio = ServicioRecetas()
  while True:
    print("\n=== MENU DE RECETAS ===")
    print("1. Crear receta")
    print("2. Listar recetas")
    print("3. Actualizar receta")
    print("4. Eliminar receta")
    print("5. Salir")
    opcion = input("Selecciona una opcion: ").strip()

    try:
      if opcion == "1":
        titulo = input("Titulo: ")
        descripcion = input("Descripcion: ")
        tiempo = input("Tiempo de preparacion (min): ")
        dificultad = input("Dificultad: ")
        instrucciones = input("Instrucciones: ")
        servicio.crear_receta(
            titulo, descripcion, tiempo, dificultad, instrucciones
        )
        print("Receta guardada correctamente.")
      elif opcion == "2":
        recetas = servicio.listar_recetas()
        if not recetas:
          print("No hay recetas registradas.")
        for r in recetas:
          print(r)
      elif opcion == "3":
        id_receta = input("ID de la receta a actualizar: ")
        titulo = input("Nuevo titulo: ")
        descripcion = input("Nueva descripcion: ")
        tiempo = input("Nuevo tiempo de preparacion (min): ")
        dificultad = input("Nueva dificultad: ")
        instrucciones = input("Nuevas instrucciones: ")
        servicio.actualizar_receta(
            id_receta, titulo, descripcion, tiempo, dificultad, instrucciones
        )
        print("Receta actualizada correctamente.")
      elif opcion == "4":
        id_receta = input("ID de la receta a eliminar: ")
        servicio.eliminar_receta(id_receta)
        print("Receta eliminada correctamente.")
      elif opcion == "5":
        print("Saliendo del sistema.")
        break
      else:
        print("Opcion invalida.")
    except Exception as e:
      print("Error:", e)