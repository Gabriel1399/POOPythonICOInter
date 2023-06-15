class Autor:
    def __init__(self, nombre, pseudonimo):
        self.__nombre = nombre
        self.__pseudonimo = pseudonimo

    @property 
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def pseudonimo(self):
        return self.__pseudonimo
    @pseudonimo.setter
    def pseudonimo(self, pseudonimo):
        self.__pseudonimo = pseudonimo

    def __str__(self):
        return f"Nombre: {self.__nombre} \nPseudonimo: {self.__pseudonimo}"
    
    def escribir(self):
        print(f" {self.__pseudonimo} está escribiendo su siguiente obra")

class Libro:
    def __init__(self, titulo, autor, año, editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__editorial = editorial

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def año(self):
        return self.__año
    @año.setter
    def año(self, año):
        self.__año = año

    @property
    def editorial(self):
        return self.__editorial
    editorial.setter
    def editorial(self, editorial):
        self.__editorial = editorial

    def __str__(self):
        return f"""
        Título: {self.__titulo}
        Autor: {self.__autor}
        Año: {self.__año}
        Editorial: {self.__editorial}
        """

    
    @classmethod
    def libro_planeta(cls, titulo, autor, año):
        return cls(titulo, autor, año, "Planeta")
    
    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")
