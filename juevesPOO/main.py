from cosas import Libro, Autor
def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrik", "PS"), 1980)
    print(l1)

    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)

main()