'''
EJERCICIO 4
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")

#mensajes iniciales
print("\t\t\tEste programa extrae las iniciales del nombre\n\n")
nom=input("ingresa el nombre: ")#El nombre es "Mauricio Gibran Colima Flores"

#Proceso
iniciales=nom[0]+nom[9]+nom[-13]+nom[-6]#Concatena todas las iniciales
print(iniciales)
print(nom[:15])#Nombres
print(nom[-13:-7])#Apellido paterno
print(nom[-6:])#Apellido materno
