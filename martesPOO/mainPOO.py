from cosas import Alumno
def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("---------------")

    al1.facultad = "FES Aragón EDOMEX"
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)

    print("----- Un vistazo a los objetos -----")

    print(vars(al1))
    print(vars(al2))

    print("----- Modificar atributos públicos -----")
    #vars ayuda a visualizar los atributos o variables del objeto
    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
    """

    al1 = Alumno("Gabriel", 23, "ICO")
    al2 = Alumno("Montse", 20, "Derecho")

    print(vars(al1))
    al1.__edad = 333
    print(al1.__edad)
    print(vars(al1))

main()