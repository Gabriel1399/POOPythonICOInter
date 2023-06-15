from cosas import Alumno
from cosas import Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))

    al1.__nombre = "Diego"
    print(vars(al1))

    print("-----To String-----")
    print(al1)

    al1.estudiar(5)
    al1.estudiar()

    print("----- PERRO -----")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #Set en notación Pythonic
    print(vars(perro1))
    perro1.__raza = "otra"
    print(vars(perro1))
    print(perro1)

    print(Perro.es_cachorro(perro1.edad))
    Perro.dormir()

    danes = Perro.perro_grande(0.8)
    print(danes)

    obj1 = Perro("Pug", 1, 0.4)
    obj2 = Perro.perro_grande(0.9)
    obj3 = Perro.constructor_dos("French", 2)

    print(obj1)
    print(obj2)
    print(obj3)

main()