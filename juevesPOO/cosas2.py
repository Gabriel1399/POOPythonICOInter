class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

class Alumno(Persona):
    def __init__(self, nombre, edad, numero_cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.__numero_cuenta = numero_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @numero_cuenta.setter
    def numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    @property
    def carrera(self):
        return self.__carrera
    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def promedio(self):
        return self.__promedio
    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio