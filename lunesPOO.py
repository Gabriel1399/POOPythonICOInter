# Esto es un comentario.
print("Hola Mundo")  # Esto imprime "Hola Mundo".
 
print("Hola", "Mundo")
 
print("Hola" + "Mundo")
 
print("Hola", "Mundo", sep="-")  # Imprime: Hola-Mundo.
 
print("Hola", end="")
print("Mundo")  # Imprime: HolaMundo.
 

# Da formato al Strig (método de la clase string (format)). 
nombre = "José"
carrera = "ICO, la mejor"
print("Mi nombre es {} y estudio {} en la FES Aragón".format(nombre, carrera))
 
# Otra manera de utilizar format, más clara.
nombre = "José"
carrera = "ICO, la mejor"
print(f"Mi nombre es { nombre} y estudio { carrera } en la FES Aragón")
 
 
 
"""
este es
un 
comentario de
múltiple línea.
"""
 
# Operadores aritméticos.
suma = 5 + 3    # 8
resta = 5 - 3   # 2
producto = 5 * 3  # 15
division = 5 / 3  # 1.66667
division2 = 5 // 3 # 1
modulo = 5 % 3   # 2
potencia = 5 ** 3  # 125
 
# Operadores de comparación.
igual = 5 == 3  # False
diferente = 5 != 3  # True
mayor_que = 5 > 3  # True
menor_que = 5 < 3  # False
mayor_o_igual_que = 5 >= 3  # True
menor_o_igual_que = 5 <= 3  # False
 
# Operadores lógicos.
y = True and False  # False
o = True or False  # True
no = not True  # False

# Cadenas de texto .
saludo = "Hola Mundo"
cita = 'Los alumnos \nde ICO\t\t \'dicen\': "Hola Mundo"'
parrafo = """Esto es un párrafo
que abarca varias
líneas"""
 
def fn_uno():
    print("Hola desde la función")

# Asignación múltiple.
a, b, c,d = 10, "Hola", fn_uno,[2.3, 3.4]
print(a)
print(b)
print(c)
print(c.__call__())
print(d[1])
 
 
# Entrada por teclado.
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola {nombre}!")
 
edad = int(input("Introduce tu edad: "))
print(f"{nombre} tiene {edad} años")
 

# Variables y tipos de datos. 
mensaje = "Hola Mundo"  # String
edad = 20               # Integer
pi = 3.14159            # Float
es_mayor = True         # Boolean
imaginario = 3 + 4j     # Imaginario

#Tipos de datos compuestos. 
frutas = ['Limón', 'Aguacate', 'Fresa']
print(frutas[2])
print(frutas[-1])

cosas = ['limón', 10, 3.1416, True, [1, 2, 3, 4], "hola"]
print(cosas)

#Slicing en Python
"""
[<inicio>: <stop>: <step>]

Es la posibilidad de obtener rebanadas a partir de un tipo de 
dato lista o tupla, en general de un iterable. Un tipo de dato 
String es iterable

por defecto
inicio = 0
stop = Tamaño de la variable
step = 1
"""

ejemplo = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e']
print(ejemplo)

rebanada = ejemplo[:6:]
print(rebanada)

#Tuplas, son inmutables
frutas_dos = ('Aguacate', 'Limón', 'Naranja')
print(frutas)
print(frutas_dos)

frutas[1] = 'Piña'
#frutas_dos[1] 0 'Piña'

print(frutas[1])
print(frutas_dos[1])

print(frutas_dos[1:2:1])
print(frutas_dos[1:2:1])

#Diccionarios 
"""
1. Es un conjunto de pares llave valor
2. Agrupados po ':
3. La llave siempre es de tipo string
4. El valor puede ser de cualquier tipo
5. El selector de la forma ['llave']
6. Mutable
7. Se declara entre los caracteres '{y}'
8. Los pares están separados por comas ','
"""

alumno= {'numero_cuenta': 1232322, 'carrera' : 'ICO', 'direccion' : {'calle': 'rancho seco', 'numero' : 23}}
print(alumno['carrera'])
print(alumno['direccion'])
print(alumno['direccion']['numero'])
print(alumno['direccion']['calle'][3:6:1])

# if.
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
 
# if-esle.
 
edad = 15
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
 
# if- elif - else.
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")
 
# if-elif-elif.
edad = 20
if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 30:
    print("Eres un joven adulto.")
 
 
 
# For   for(int = 1 ; i<10 ; i++).
 
for i in range(1, 10, 1):
    print(i)
 
frutas = ['piña', 'pera', 'manzana', 'fresa', 'aguacate']
for numero in frutas:
    print(numero)
 
for numero in frutas:
    if numero == "manzana":
        break   # ó continue
    print(numero)  # imprime la fruta
 
 
 
 
# ------------- como usar   ------------
 
import aritmetica
 
resultado = aritmetica.suma(5, 3)
print(resultado)
 
#--------------- solo unas
from aritmetica import suma, resta
 
print(suma(5, 3))
print(resta(5, 3))
 
 
# ---------renombrar
 
import aritmetica as ari
 
resultado = ari.suma(4, 3)
print(resultado)
 
 
# escepciones
 
 
try:
    numero = 1 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero")