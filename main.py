rom datetime import datetime

class Libro:
    def __init__(self, titulo, autor, editorial, ano_publicacion, isbn, precio=0):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_publicacion = ano_publicacion
        self.isbn = isbn
        self.disponible = True
        self.precio = precio


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.ventas = []
        self.usuarios = {}

    def registar_usuario(self, nombre, telefono, correo):
        nuevo_usuario = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        }


    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None

    def buscar_libro_por_autor(self, autor):
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor == autor:
                libros_encontrados.append(libro)
        return libros_encontrados

    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            libro.disponible = False
        else:
            print("El libro que buscas no está disponible")

    def devolver_libro(self, libro):
        libro.disponible = True

    def vender_libro(self, libro):
        if libro.disponible:
            self.eliminar_libro(libro)
            libro.disponible = False
            print(f"libro vendido: {libro.titulo}")
        else:
            print("el libro ha sido prestado y no puede ser vendido")

libro1 = Libro("El Quijote", "Miguel de Cervantes", "Editorial Castalia", 1605, "978-84-7039-455-6", 22.25)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Editorial Sudamericana", 1967, "978-987-566-567-1", 18.00)
libro3 = Libro("Rayuela", "Julio Cortázar", "Editorial Sudamericana", 1963, "978-950-07-4726-1", 13.75)
libro4 = Libro("La metamorfosis", "Franz Kafka", "Editorial Losada", 1915, "978-950-03-0159-9", 12.25)
libro5 = Libro("1984", "George Orwell", "Editorial Seix Barral", 1949, "978-843-221-228-9", 10.00)

# Crear una biblioteca y agregar algunos libros
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

# Solicitar al usuario el título del libro a prestar
titulo_libro_prestar = input("Ingrese el título del libro que desea prestar: ")

# Buscar el libro correspondiente en la biblioteca
libro_prestar = biblioteca.buscar_libro_por_titulo(titulo_libro_prestar)


# Verificar si el libro está disponible y prestarlo si es posible
if libro_prestar:
    if libro_prestar.disponible:
        biblioteca.prestar_libro(libro_prestar, "Juan")
        print(f"Libro prestado: {libro_prestar.titulo}")
        libro_prestar = True
    else:
        print("El libro no está disponible")
else:
    print("Libro no encontrado")
#holaasdsadsad

# Solicitar al usuario el título del libro a devolver

if libro_prestar == True:
    titulo_libro_devolver = input("Ingrese el título del libro que desea devolver: ")
# Buscar el libro correspondiente en la biblioteca
    libro_devolver = biblioteca.buscar_libro_por_titulo(titulo_libro_devolver)
# Devolver el libro si se encuentra en la biblioteca
    if libro_devolver:
        biblioteca.devolver_libro(libro_devolver)
        print(f"Libro devuelto: {libro_devolver.titulo}")
    else:
        print("Libro no encontrado")

#libro que desea vender
titulo_libro_vender = input("Ingrese el título del libro que desea vender: ")
libro_vender = biblioteca.buscar_libro_por_titulo(titulo_libro_vender)

if libro_vender:
    if libro_vender.disponible:
        biblioteca.vender_libro(libro_vender)
    else:
        print("El libro no está disponible para la venta")
else:
    print("Libro no encontrado")
