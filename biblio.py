# Creando la clase Libro

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo      
        self.autor = autor        
        self.isbn = isbn         
        self.disponible = True  




# Lista para almacenar los libros


biblioteca = []




# 1.Función para agregar un nuevo libro a la lista biblioteca mediante inputs del usuario


def agregar():
  
    print("\nAgregar un nuevo libro:\n")
    titulo = input("> Título: ")
    autor = input("> Autor: ")
    isbn = input("> ISBN: ")

    # Crear un nuevo objeto Libro con los valores introducidor por el usuario y lo añade la lista biblioteca
    nuevo_libro = Libro(titulo, autor, isbn)
    biblioteca.append(nuevo_libro)
    print(f"\nTítulo: {titulo}\nAutor:{autor}\nISBN:{isbn}\nLibro agregado con éxito.\n")




# 2. Función para prestar un libro a apartir de su ISBN


def prestar():

    isbn = input("\n> Introduce el ISBN: ") #Usuario introduce el ISBN

    libro_encontrado = False #Variable para saber si se ha encontrado el libro. Por defecto se pone en False

    for libro in biblioteca: #Recorre la lista de libros con un bucle for

        if libro.isbn == isbn: #si el ISBN del libro es igual al ISBN introducido por el usario.

            if libro.disponible == True:

                libro.disponible = False

                print(f"\n- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Prestado con éxito.\n") 

            else:
                 
                 print(f"\n- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - No está disponible.\n") 

            libro_encontrado = True #Libro encontrado cambia a True

            break #Hemos encontrado el libro, salimos del bucle

    if libro_encontrado==False:

        print("\n[!] No existe ese ISBN\n")



# 3. Función para devolver un libro a apartir de su ISBN

def devolver():

    isbn = input("\n> Introduce el ISBN: ") #Usuario introduce el ISBN

    libro_encontrado = False #Variable para saber si se ha encontrado el libro. Por defecto se pone en False

    for libro in biblioteca: #Recorre la lista de libros con un bucle for

        if libro.isbn == isbn: #si el ISBN del libro es igual al ISBN introducido por el usario.

            if libro.disponible == False:

                libro.disponible = True

                print(f"\n- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Devolución realizada con éxito.\n") 

            else:
                 
                 print(f"\n- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Libro disponible para prestar.\n") 

            libro_encontrado = True #Libro encontrado cambia a True

            break #Hemos encontrado el libro, salimos del bucle

    if libro_encontrado==False:

        print("\n[!] No existe ese ISBN\n")



# 4. Función para mostrar todos los libros y su estado

def mostrar():

    if not biblioteca:

        print("\nNo hay libros guardados.")

    else:

        print("\nLibros disponibles:")
      
        for libro in biblioteca:

            #Imprime los datos de los libros don un format
            print(f"\n- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {'Sí' if libro.disponible else 'No'}")      




#5. Función para buscar un libro por su ISBN

def buscar():

    isbn = input("\n> Introduce el ISBN: ") #Usuario introduce el ISBN

    libro_encontrado = False #Variable para saber si se ha encontrado el libro de inicio se pone en False

    for libro in biblioteca: #Recorre la lista de libros con un bucle for

        if libro.isbn == isbn: #si el ISBN del libro es igual al ISBN introducido por el usuario se imprime los datos del libro

            print(f"\n- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {'Sí' if libro.disponible else 'No'}\n") 

            libro_encontrado = True #Libro encontrado se pone en True

            break #Hemos encontrado el libro, salimos del bucle

    if libro_encontrado==False:

        print("\n[!] No existe ese ISBN/n")


          
   
# Menú principal

print("\nBienvenido al Sistema de Gestión de Biblioteca\n")

while True: #Es una forma de generar un bucle infinito y que el menú siempre esté presente hasta que entre un break

    #Las opciones disponibles en el menú que ve el usuario
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar")
    print("6. Salir")
    
    opcion = input("\nSeleccionar opción: ") #La opción que el usuario selecciona se guarda en la variable

    if opcion == "1":
        agregar()

    elif opcion == "2":
         prestar()

    elif opcion == "3":
         devolver()
    
    elif opcion == "4":
         mostrar()

    elif opcion == "5":
         buscar()
    
    elif opcion == "6":
         
         print("\nSaliendo del Sistema de Gestión de Biblioteca...")

         print("Hasta la próxima")

         break #Salir del bucle infinito

    else:

        print("Opción no válida. Por favor, seleccionar una opción válida.")




""" 
    Script creado por Pedro Garrido para el curso de Python organizado por Bejob 2025.
    tsid.pedro.garrido@gmail.com  

"""