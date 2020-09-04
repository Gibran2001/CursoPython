'''
EJERCICIO 7
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
i=1
while(i<=n):
    x=x*i
    i=i+1
print("El factorial de tu numero es: "+str(x))