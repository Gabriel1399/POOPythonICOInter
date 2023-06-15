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

alumno= {'numero_cuenta': 1232322, 'carrera' : 'ICO', 'direccion' : 
         {'calle': 'rancho seco', 'numero' : 23}, 'telefonos': [5566478757, 4578394867]}
print(alumno['carrera'])
print(alumno['direccion'])
print(alumno['direccion']['numero'])
print(alumno['direccion']['calle'][3:6:1])
print(alumno['telefonos'])

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
 
 
 
# For   for(int i = 1 ; i<10 ; i++).
 
for i in range(1, 10, 1):
    print(i)
 
frutas = ['piña', 'pera', 'manzana', 'fresa', 'aguacate']
for fruta in frutas:
    print(fruta)

print("------------------")
 
for fruta in frutas:
    if fruta == "manzana":
        break   # break (rompe el ciclo actual) ó continue (rompe la iteación actual)
    print(fruta)  # imprime la fruta
 
tam = 0
while tam < 10:
    print(tam)
    tam(int(input("Dame un número entero: ")))
print("Final")
 
 
 
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