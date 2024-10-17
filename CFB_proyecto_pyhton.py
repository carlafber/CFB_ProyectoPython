#Se importan las librerías necesarias para ejecutar el porograma
import json
import os
import requests

# Se crea una clase que representa un libro en la biblioteca
class Libro():
    def __init__(self, titulo, autor, ano, editorial, genero): #Método para inicializar la clase
        #Asignación de los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editorial = editorial
        self.genero = genero
    def obtener_libro(self): #Método para obtener todos los datos del libro
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.ano}, Editorial: {self.editorial}, Género: {self.genero}"


# Función para agregar un nuevo libro a la biblioteca
def agregar_libro():
    print("Para agregar un libro, introduzca los siguientes datos:")
    titulo = input("Título: ") #Se solicita el título del libro
    for libro in libros: #Se verifica si el libro ya existe en la lista de libros
        if libro.titulo.lower() == titulo.lower(): #Se compara el título de manera insensible a mayúsculas
            titulo = input("El libro ya existe, introduzca otro: ") #Se pide un nuevo título si ya existe
            return #Se sale de la función si el libro ya existe
    #Se solicitan el resto de parámetros del libro
    autor = input("Autor: ")
    ano = input("Año: ")
    editorial = input("Editorial: ")
    genero = input("Género: ")
    libro_nuevo = Libro(titulo, autor, ano, editorial, genero) #Se crea un nuevo objeto Libro con los datos proporcionados
    libros.append(libro_nuevo) #Se agrega el nuevo libro a la lista
    print("\nLibro agregado correctamente.") #Mensaje de confirmación


# Función para buscar un libro por su título
def buscar_libro_titulo():
    titulo = input("Para buscar un libro, introduzca el título: ") #Se solicita el título del libro a buscar
    for libro in libros: #Se itera sobre los libros para encontrar coincidencias
        if libro.titulo.lower() == titulo.lower(): #Se compara el título de manera insensible a mayúsculas
            print("\nLIBRO\n" + libro.obtener_libro()) #Se muestran los detalles del libro encontrado
            return
    print(f'\nNo se encontró ningún libro con el título "{titulo}".') #Mensaje si no se encuentra el libro


# Función para buscar libros por autor
def buscar_libro_autor():
    autor = input("Para buscar un libro, introduzca su autor: ") #Se solicita el autor a buscar
    libros_autor = list(filter(lambda libro: libro.autor.lower() == autor.lower(), libros)) #Filter y lambda para encontrar libros que coincidan con el autor
    if libros_autor: #Se verifica si se encontraron libros
        print("\nLIBROS:")
        for libro in libros_autor:
            print(libro.obtener_libro()) #Se muestran los detalles de cada libro encontrado
    else:
        print(f'\nNo se encontró ningún libro del autor "{autor}".') #Mensaje si no se encuentra ningún libro


# Función para buscar libros por género
def buscar_libro_genero():
    genero = input("Para buscar libros, introduzca su género: ") #Se solicita el género a buscar
    libros_genero = list(filter(lambda libro: libro.genero.lower() == genero.lower(), libros)) #Filter y lambda para encontrar libros que coincidan con el género
    if libros_genero: #Se verifica si se encontraron libros
        print("\nLIBROS:")
        for libro in libros_genero:
            print(libro.obtener_libro()) #Se muestran los detalles de cada libro encontrado
    else:
        print(f'\nNo se encontró ningún libro del género "{genero}".') #Mensaje si no se encuentra ningún libro


# Función para mostrar todos los libros en la biblioteca
def mostrar_libros():
    if libros: #Se verifica si hay libros en la lista
        print("\nLIBROS DE LA BIBLIOTECA:")
        for libro in libros:
            print(libro.obtener_libro()) #Se muestran los detalles de cada libro
    else:
        ("\nNo hay ningún libro en la biblioteca.") #Mensaje si la biblioteca está vacía     


# Función para actualizar la información de un libro
def actualizar_libro():
    titulo = input("Para actualizar un libro, introduzca el título: ") #Se solicita el título del libro a actualizar
    for libro in libros: #Se itera sobre los libros
        if libro.titulo.lower() == titulo.lower(): #Se compara el título ingorando las mayúsculas
            print(f"\nLibro encontrado: {libro.obtener_libro()}") #Se muestran los detalles del libro encontrado 
            opcion = 0 #Se inicializa la opción de actualización a 0, una opción que no existe
            # Bucle para actualizar campos específicos del libro
            while (opcion != 5): 
                print("\n¿Qué campo desea actualizar?") #Se solicita al usuario qué campo quiere actualizar
                print("1. Autor")
                print("2. Año")
                print("3. Editorial")
                print("4. Género")
                print("5. Terminar la actualización")
                try:
                    opcion = int(input("Selecciona una opción (1-5): ")) #Se solicita una opción al usuario
                except ValueError: #Manejo de errores si la entrada no es un número
                    print("Error: Debes introducir un número válido.")
                    continue
                
                # Estructura de control para manejar la opción seleccionada
                match opcion:
                    case 1: #Se actualiza el autor
                        nuevo_autor = input("\nIntroduzca el nuevo autor: ")
                        if nuevo_autor: #Se verifica si se ingresó un nuevo autor
                            libro.autor = nuevo_autor #Se actualiza el autor
                            print("Autor actualizado.")
                    case 2: #Se actualiza el año
                        nuevo_ano = input("\nIntroduzca el nuevo año: ")
                        if nuevo_ano: #Se verifica si se ingresó un nuevo año
                            libro.ano = nuevo_ano #Se actualiza el año
                            print("Año actualizado.")
                    case 3: #Se actualiza la editorial
                        nueva_editorial = input("\nIntroduzca la nueva editorial: ")
                        if nueva_editorial: #Se verifica si se ingresó una nueva editorial
                            libro.editorial = nueva_editorial #Se actualiza la editorial
                            print("Editorial actualizada.")
                    case 4: #Se actualiza el género
                        nuevo_genero = input("\nIntroduzca el nuevo géreno: ")
                        if nuevo_genero: #Se verifica si se ingresó un nuevo género
                            libro.genero = nuevo_genero #Se actualiza el género
                            print("Género actualizado.")
                    case 5: #Se termina la actualización
                        print("\nActualización finalizada.")
                        break
                    case _: #Manejo de opción no válida
                        print("\nOpción no válida. Intente de nuevo.")
            return #Se sale de la función

# Función para buscar información adicional de un libro usando una API externa
def buscar_info_api():
    titulo = input("Introduzca el título del libro para buscar información adicional: ") #Se solicita el título del libro
    url = f"https://www.googleapis.com/books/v1/volumes?q={titulo}" #Se construye la URL para la API de Google Books
    response = requests.get(url) #Se realiza la solicitud HTTP GET a la API

    if response.status_code == 200: #Se verifica si la solicitud fue exitosa
        data = response.json() #Se convierte la respuesta a formato JSON
        if 'items' in data: #Se verifica si hay libros en los resultados
            item = data['items'][0] #Se toma solo el primer resultado
            title = item['volumeInfo'].get('title', 'Sin título') #Se obtiene el título del libro
            authors = item['volumeInfo'].get('authors', 'Sin autor') #Se obtiene el autor
            published_date = item['volumeInfo'].get('publishedDate', 'Sin fecha de publicación')  #Se obtiene la fecha de publicación
            description = item['volumeInfo'].get('description', 'Sin descripción')  #Se obtiene la descripción del libro
            print(f"\nTítulo: {title}\nAutor: {', '.join(authors)}\nFecha de Publicación: {published_date}\nDescripción: {description}\n") #Se muestra la información del libro
        else:
            print("No se encontraron resultados para este libro.") #Mensaje si no se encuentran resultados
    else:
        print(f"Error en la petición a la API: {response.status_code}") #Mensaje de error en la solicitud


# Función para guardar los datos en un archivo JSON
def guardar_datos():
    with open(nombre_archivo, 'w') as archivo:  #Se abre el archivo en modo escritura ('w')
        libros_json = [libro.__dict__ for libro in libros]  #Se convierten los objetos a diccionarios y se usa __dict__ para cada objeto
        json.dump(libros_json, archivo, indent=4) #Se guarda la lista en el archivo en formato JSON, añadiendo indentación para que sea más legible
    print("Datos guardados correctamente.") #Mensaje de confirmación


# Función para cargar los datos desde un archivo JSON
def cargar_datos():
    try:
        with open('biblioteca.json', 'r') as archivo:  #Se intenta abrir el archivo en modo lectura ('r')
            libros_json = json.load(archivo) #Se carga el contenido del archivo en formato JSON
            return [Libro(**libro) for libro in libros_json] #Se convierte cada diccionario a un objeto de tipo 'Libro' y se devuelve la lista
    except (FileNotFoundError, json.JSONDecodeError):
        return [] #Si el archivo no existe o hay error en el formato JSON, se retorna una lista vacía


nombre_archivo = 'biblioteca.json' #Nombre del archivo donde se guardarán los datos
libros = cargar_datos() #Se cargan los datos iniciales desde el archivo (si existe)
opcion = -1 #Se incializa la opción en -1 para que el menú se muestre al menos una vez

# Bucle que mantiene el menú activo hasta que el usuario decida salir (opción 0)
while (opcion != 0):
    print("\nBIBLIOTECA\n1. Agregar libro\n2. Buscar libro por título\n3. Buscar libros por autor" + 
        "\n4. Buscar libros por género\n5. Mostrar todos los libros\n6. Actualizar libro" +
        "\n7. Buscar información adicional en API\n8. Guardar datos en un fichero\n9. Eliminar el fichero" + 
        "\n----------------------------------------\n0. Salir") #Se muestra el menú de opciones
    
    try: #Se intenta obtener una opción válida del usuario
        opcion = int(input("Selecciona una opción: ")) #Se convierte la entrada a entero
    except ValueError:
        print("Error: Debes introducir un número válido.") #Si el usuario ingresa un valor no válido (no numérico), se muestra un mensaje de error
        continue #Se vuelve a mostrar el menú
    
    # Estructura de control para manejar la opción seleccionada, en cada case se llama a la función necesaria para realizar acciones libros
    match opcion:
        case 1:
            agregar_libro()
        case 2:
            buscar_libro_titulo()
        case 3:
            buscar_libro_autor()
        case 4:
            buscar_libro_genero()
        case 5:
            mostrar_libros()
        case 6:
            actualizar_libro()
        case 7:
            buscar_info_api()
        case 8:
            guardar_datos()
        case 9:
            os.remove(nombre_archivo) #Se elimina el archivo si existe
            print(f"Fichero {nombre_archivo} eliminado correctamente.")
        case 0:
            print("Saliendo...") #Si el usuario selecciona la opción 0, el programa termina
            exit() #Se sale del programa
        case _:
            print("Error") #Mensaje en caso de que el usuario seleccione una opción no válida