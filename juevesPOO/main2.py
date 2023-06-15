from cosas2 import Alumno

def main():
    print("----- Herencia ------")
    al1 = Alumno("José", 19, "23232", "ICO", 9)
    al1.nombre = "Pepe"
    print(vars(al1))


main()