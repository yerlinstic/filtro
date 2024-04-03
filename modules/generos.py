class generos:
  

    def listar_generos(self):
        generos = set() 
        for pelicula in self.peliculas.values():
            generos.add(pelicula.genero)
        
        if generos:
            print("\nLista de géneros disponibles:")
            for genero in generos:
                print("- {}".format(genero))
        else:
            print("No hay géneros disponibles en el sistema.")

def main():
    app = generos()

    while True:
        Bienvenido_menu()

        print("\nBienvenido al sistema de gestión de películas\n")
        print("1. Agregar película")
        print("2. Eliminar película")
        print("3. Buscar película por código")
        print("4. Mostrar películas por género")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            agregar_pelicula(app)
        elif opcion == "2":
            eliminar_pelicula(app)
        elif opcion == "3":
            buscar_pelicula_por_codigo(app)
        elif opcion == "4":
            app.listar_generos() 
        elif opcion == "5":
            buscar_pelicula_por_genero()
        elif opcion == "6":
            guardar_datos(app)
        elif opcion == "7":
            cargar_datos(app)
        elif opcion == "8":
            app.listar_peliculas()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
        
        
        
