import json
import modules.atores as actores
import modules.formato as formato
import modules.generos as generos
import modules.informacion as informacion
import modules.pelicula as pelicula

class Pelicula:
    def __init__(self, codigo, nombre, genero, duracion, actores):
        self.codigo = codigo
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.actores = actores

class Actores:
    def __init__(self, id, nombre, rol):
        self.id = id
        self.nombre = nombre
        self.rol = rol

class BlockbusterApp:
    def __init__(self):
        self.peliculas = {}

    def agregar_pelicula(self, pelicula):
        self.peliculas[pelicula.codigo] = pelicula

    def eliminar_pelicula(self, codigo):                                                    
        if codigo in self.peliculas:
            del self.peliculas[codigo]
        else:
            print("La película con el código {} no existe.".format(codigo))

    def buscar_pelicula_por_genero(self, genero):
        return [p for p in self.peliculas.values() if p.genero == genero]

    def buscar_pelicula_por_codigo(self, codigo):
        if codigo in self.peliculas:
            return self.peliculas[codigo]
        else:
            return None

    def guardar_datos(self, archivo):
            peliculas_data = []
            for pelicula in self.peliculas.values():
                pelicula_data = {
                    'codigo': pelicula.codigo,
                    'nombre': pelicula.nombre,
                    'genero': pelicula.genero,
                    'duracion': pelicula.duracion,
                    'actores': [
                        {'id': actor.id, 'nombre': actor.nombre, 'rol': actor.rol}
                        for actor in pelicula.actores
                    ]
                }
                peliculas_data.append(pelicula_data)
            json.dump(peliculas_data, fileindent=4)

    def cargar_datos(self, archivo):    
        with open(archivo, 'r') as file:
            peliculas_data = json.load(file)
            for pelicula_data in peliculas_data:
                actores = [
                    Actores(actor_data['id'], actor_data['nombre'], actor_data['rol'])
                    for actor_data in pelicula_data['actores']
                ]
                pelicula = Pelicula(pelicula_data['codigo'], pelicula_data['nombre'],
                                    pelicula_data['genero'], pelicula_data['duracion'], actores)
                self.agregar_pelicula(pelicula)

def gestionar_activos(app):
    while True:
        print("""
       
              
              
               print("1. Agregar película")
        print("2. Eliminar película")
        print("3. Buscar película por código")
        print("4. Mostrar películas por género")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")
""")
        opcion = input("Selecciona una opción: ")

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def agregar_pelicula(app):
    codigo = input("Ingrese el código de la película: ")
    nombre = input("Ingrese el nombre de la película: ")
    genero = input("Ingrese el género de la película: ")
    duracion = input("Ingrese la duración de la película: ")
    num_actores = int(input("Ingrese el número de actores: "))
    actores = []
    for i in range(num_actores):
        id = input("Ingrese el ID del actor {}: ".format(i+1))
        nombre_actor = input("Ingrese el nombre del actor {}: ".format(i+1))
        rol = input("Ingrese el rol del actor {}: ".format(i+1))
        actores.append(Actores(id, nombre_actor, rol))
    pelicula = Pelicula(codigo, nombre, genero, duracion, actores)
    app.agregar_pelicula(pelicula)
    print("Película agregada exitosamente.")

def eliminar_pelicula(app):
    codigo = input("Ingrese el código de la película a eliminar: ")
    app.eliminar_pelicula(codigo)

def buscar_pelicula_por_codigo(app):
    codigo = input("Ingrese el código de la película a buscar: ")
    pelicula = app.buscar_pelicula_por_codigo(codigo)
    if pelicula:
        print("Película encontrada:", pelicula.nombre)
    else:
        print("Película no encontrada.")

def buscar_pelicula_por_genero(app):
    genero = input("Ingrese el género de la película a buscar: ")
    peliculas = app.buscar_pelicula_por_genero(genero)
    if peliculas:
        print("Películas encontradas del género '{}':".format(genero))
        for pelicula in peliculas:
            print("- {}".format(pelicula.nombre))
    else:
        print("No hay películas del género '{}'.".format(genero))

def guardar_datos(app):
    archivo = input("Ingrese el nombre del archivo para guardar los datos: ")
    app.guardar_datos(archivo)
    print("Datos guardados exitosamente.")

def cargar_datos(app):
    archivo = input("Ingrese el nombre del archivo para cargar los datos: ")
    app.cargar_datos(archivo)
    print("Datos cargados exitosamente.")

def main():
    app = BlockbusterApp()
    gestionar_activos(app)

if __name__ == "__main__":
    main()





def gestionar_activos(app):
    while True:
        print("\nBienvenido \n")
        print("1. Agregar película")
        print("2. Eliminar película")
        print("3. Buscar película por código")
        print("4. Mostrar películas por género")
        print("5. Guardar datos")
        print("6. Cargar datos")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

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
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")




