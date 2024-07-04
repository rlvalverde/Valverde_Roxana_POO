class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

# Clase Empleado que hereda de Persona
class Empleado(Persona):
    # Constructor de la clase Empleado
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    # Método sobrescrito para mostrar la información del empleado
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f'{info_base}, Salario: {self.salario}'

# Clase CuentaBancaria demostrando encapsulación
class CuentaBancaria:
    # Constructor de la clase CuentaBancaria
    def __init__(self, titular, balance):
        self.__titular = titular
        self.__balance = balance

    # Getter para el balance
    def get_balance(self):
        return self.__balance

    # Setter para el balance
    def set_balance(self, nuevo_balance):
        if nuevo_balance >= 0:
            self.__balance = nuevo_balance
        else:
            print("El balance no puede ser negativo")

    # Método para mostrar la información de la cuenta
    def mostrar_info(self):
        return f'Titular: {self.__titular}, Balance: {self.__balance}'

# Clase Animal demostrando polimorfismo
class Animal:
    # Método abstracto para hacer sonido
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

# Clase Perro que hereda de Animal
class Perro(Animal):
    # Método sobrescrito para hacer sonido
    def hacer_sonido(self):
        return "Guau!"

# Clase Gato que hereda de Animal
class Gato(Animal):
    # Método sobrescrito para hacer sonido
    def hacer_sonido(self):
        return "Miau!"

# Crear instancia de Empleado
empleado1 = Empleado('Juan', 30, 50000)
print(empleado1.mostrar_info())

# Crear instancia de CuentaBancaria
cuenta = CuentaBancaria('Ana', 1000)
print(cuenta.mostrar_info())
cuenta.set_balance(1500)
print(cuenta.get_balance())

# Crear instancias de Perro y Gato y demostrar polimorfismo
animales = [Perro(), Gato()]
for animal in animales:
    print(animal.hacer_sonido())
