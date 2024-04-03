class BlockbusterApp:
    def listar_peliculas(self):
        if self.peliculas:
            print("\nLista de películas:")
            for pelicula in self.peliculas.values():
                print("Código: {}, Nombre: {}, Género: {}, Duración: {} minutos".format(
                    pelicula.codigo, pelicula.nombre, pelicula.genero, pelicula.duracion))
        else:
            print("No hay películas en el sistema.")

def main():
    app = BlockbusterApp()

    while True:
        mostrar_menu()

        opcion = input("\nSelecciona una opción: ")

        
        print("\nBienvenido al sistema de gestión de películas\n")
        print("1. Agregar película")
        print("2. Eliminar película")
        print("3. Buscar película por código")
        print("4. Mostrar películas por género")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")
        
        
        if opcion == "1":
            agregar_pelicula(app)
        elif opcion == "2":
            eliminar_pelicula(app)
        elif opcion == "3":
            buscar_pelicula_por_codigo(app)
        elif opcion == "4":
            buscar_pelicula_por_genero(app)
        elif opcion == "5":
            guardar_datos(app)
        elif opcion == "6":
            cargar_datos(app)
        elif opcion == "7":
            app.listar_peliculas()  
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
        
        
        
        
        
        
        
