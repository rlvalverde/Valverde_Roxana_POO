"""
Este programa gestiona un registro básico de estudiantes.
Permite añadir estudiantes, listar estudiantes y calcular la edad promedio.
Utiliza diferentes tipos de datos como enteros, cadenas y booleanos.
"""
def añadir_estudiante(estudiantes, nombre, edad, genero):
    """
    Esta función añade un estudiante al registro.
    :param estudiantes: Lista de estudiantes (list)
    :param nombre: Nombre del estudiante (str)
    :param edad: Edad del estudiante (int)
    :param genero: Género del estudiante (str)
    """
    estudiantes.append({"nombre": nombre, "edad": edad, "genero": genero})

def listar_estudiantes(estudiantes):
    """
    Esta función lista todos los estudiantes en el registro.
    :param estudiantes: Lista de estudiantes (list)
    """
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Género: {estudiante['genero']}")

def calcular_edad_promedio(estudiantes):
    """
    Esta función calcula la edad promedio de los estudiantes.
    :param estudiantes: Lista de estudiantes (list)
    :return: Edad promedio (float)
    """
    total_edad = sum(estudiante["edad"] for estudiante in estudiantes)
    return total_edad / len(estudiantes) if estudiantes else 0.0

def main():
    estudiantes = []

    # Añadir algunos estudiantes
    añadir_estudiante(estudiantes, "Juan Perez", 20, "Masculino")
    añadir_estudiante(estudiantes, "Ana Gomez", 22, "Femenino")
    añadir_estudiante(estudiantes, "Luis Rodriguez", 21, "Masculino")

    # Listar los estudiantes
    print("Lista de Estudiantes:")
    listar_estudiantes(estudiantes)

    # Calcular y mostrar la edad promedio
    edad_promedio = calcular_edad_promedio(estudiantes)
    print(f"\nEdad promedio de los estudiantes: {edad_promedio:.2f} años")

    # Uso de una cadena y un booleano
    mensaje = "Operación completada exitosamente"
    exito = True  # boolean

    print(mensaje)
    if exito:
        print("El programa se ejecutó correctamente.")

if __name__ == "__main__":
    main()