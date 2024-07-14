class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Persona.

        Args:
        - nombre (str): Nombre de la persona.
        - edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f'Se ha creado una nueva persona llamada {self.nombre}')

    def __del__(self):
        """
        Destructor de la clase Persona.
        Se ejecuta cuando el objeto es destruido.
        """
        print(f'La persona {self.nombre} ha sido eliminada')


# Ejemplo de uso de la clase Persona
if __name__ == "__main__":
    # Creamos una instancia de Persona
    persona1 = Persona("Juan", 30)

    # Creamos otra instancia de Persona
    persona2 = Persona("María", 25)

    # Eliminamos la instancia persona1
    del persona1

    # Al finalizar el programa, persona2 será eliminada automáticamente
