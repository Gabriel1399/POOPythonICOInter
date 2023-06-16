from cosas import *

def main():
    persona1 = Persona("Jose", 19)
    print(persona1)
    print(Persona.descripcion)

    print("")
    print("-----Herencia alumno-----")
    alumno1 = Alumno("José", 19, "2344456456", "ICO")
    print(alumno1)
    print(Alumno.descripcion)

    alumno2 = Alumno.constructor_defecto()
    print(alumno2)
    alumno2.nombre = "Juan"
    print(alumno2)
    alumno2.dormir()

    print("")
    print("-----Herencia profesor-----")
    profesor1 = Profesor("Jesús", 30+16, 363565, "Ingeniería")
    print(profesor1)
    profesor1.dormir()

    print("")
    print("-----Herencia multiple (ayudante profesor)-----")
    ayudante = AyudanteProfesor("Adrián", 20, "64798", "ICO", "56984", "Ingeniería de Software", 4)
    print(ayudante)
    ayudante.dormir()


main()