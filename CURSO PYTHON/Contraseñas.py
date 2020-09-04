'''
TAREA 3
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")

#Mensajes iniciales
print("\t\t\tEste programa genera contraseñas a partir de tu nombre y edad\n\n")
nom=input("Ingresa tu nombre por favor (Ej. Mauricio): ")

#Proceso
print("\n\nHola "+nom)#Saludo
print("\nTu nombre en mayúsculas es: "+nom.upper())#Mayusculas
print("\nTu nombre en minúsculas es: "+nom.lower())#Minusculas
edad=int(input("\n\nIngresa tu edad: "))
n=(3*edad)/2
cont=nom[2]+str(n)+nom[0].lower()

#Muestra el resultado
print("Tu contraseña personalizada es "+cont)
