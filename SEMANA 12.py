class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        return self.libros_prestados

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario={self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {isbn: Libro}
        self.usuarios = {}  # Diccionario {id_usuario: Usuario}
        self.isbn_prestados = set()  # Para evitar prestar el mismo libro más de una vez

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo} añadido a la biblioteca.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros and isbn not in self.isbn_prestados:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se puede eliminar el libro con ISBN {isbn} porque no existe o está prestado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios and len(self.usuarios[id_usuario].libros_prestados) == 0:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se puede dar de baja al usuario {id_usuario}. Puede que tenga libros prestados.")

    def prestar_libro(self, id_usuario, isbn):
        if isbn in self.libros and id_usuario in self.usuarios:
            if isbn not in self.isbn_prestados:
                libro = self.libros[isbn]
                self.usuarios[id_usuario].prestar_libro(libro)
                self.isbn_prestados.add(isbn)
                print(f"Libro {libro.titulo} prestado a {self.usuarios[id_usuario].nombre}.")
            else:
                print(f"El libro con ISBN {isbn} ya está prestado.")
        else:
            print(f"No se puede prestar el libro con ISBN {isbn} al usuario con ID {id_usuario}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            libro = self.usuarios[id_usuario].devolver_libro(isbn)
            if libro:
                self.isbn_prestados.remove(isbn)
                print(f"Libro {libro.titulo} devuelto por {self.usuarios[id_usuario].nombre}.")
            else:
                print(f"El usuario con ID {id_usuario} no tiene el libro con ISBN {isbn} prestado.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def buscar_libro(self, **criterios):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, key) == value for key, value in criterios.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].listar_libros_prestados()
        return []

# Ejemplo de uso
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("1984", "George Orwell", "Ficción", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "0987654321")

biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Ana", 1)
usuario2 = Usuario("Luis", 2)

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro(1, "1234567890")

# Listar libros prestados de un usuario
print(usuario1.listar_libros_prestados())

# Devolver libros
biblioteca.devolver_libro(1, "1234567890")

# Buscar libros por categoría
resultados = biblioteca.buscar_libro(categoria="Ficción")
print(resultados)

