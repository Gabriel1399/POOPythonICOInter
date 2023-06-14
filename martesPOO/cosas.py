class Alumno:
 # Atributo de clase
 facultad = "FES Aragón"

 # Constructor 
 def __init__(self, nom, ed, carr):
   # Atributo de instalncia
   self.__nombre = nom
   self.__edad = ed
   self.__carrera = carr