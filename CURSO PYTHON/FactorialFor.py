'''
EJERCICIO 6
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")

#mensajes iniciales
print("\t\t\tEste programa calcula el factorial de un numero\n\n")
n=int(input("Ingresa un numero para calcular su factorial: "))

#Proceso
x=1
for i in range(1,n+1):
    x=x*i
print("El factorial de tu numero es " +str(x))