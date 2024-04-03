class informacion:
   
    def mostrar_informacion_general(self):
        cantidad_peliculas = len(self.peliculas)
        duracion_total = sum(pelicula.duracion for pelicula in self.peliculas.values())
        duracion_promedio = duracion_total / cantidad_peliculas if cantidad_peliculas > 0 else 0

        print("\nInformación general del sistema:")
        print("Total de películas: {}".format(cantidad_peliculas))
        print("Duración promedio de las películas: {:.2f} minutos".format(duracion_promedio))

def main():
    app = informacion()

    while True:
        mostrar_menu()

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
            buscar_pelicula_por_genero(app)
        elif opcion == "6":
            guardar_datos(app)
        elif opcion == "7":
            cargar_datos(app)
        elif opcion == "8":
            app.listar_peliculas()
        elif opcion == "9":
            app.mostrar_informacion_general()  # Llamar a la función para mostrar información general
        elif opcion == "10":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

