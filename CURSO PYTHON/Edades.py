'''
EJERCICIO 3
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")

#mensaje de bienvenida
print("\n\n\t\tEste es un programa que calcula tu año de nacimiendo en base en tu edad\n")
print("*Tenga en cuenta que este programa fue creado en 2020, por favor introduzca la edad que cumpla en este año\n\n")

#El usuario ingresa su edad
edad=input("Ingresa tu edad: ")

#Hace el cálculo del año
nacimiento=2020-int(edad)#Hacemos la primera conversion vista en el curso

#Muestra el año de nacimiento
print("El año en el que naciste es:"+str(nacimiento))
