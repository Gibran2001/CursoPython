'''
TAREA 4
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")

#mensajes iniciales
print("\t\t\tEste programa convierte un número binario de 4 bits, a decimal\n\n")
n=input("Ingresa tu número binario de 4 bits: ")

#Proceso
if(len(n)==4):#Condicion, si el usuario ingresa un numero de 4 bits
    if (n[0] == '1'):#2^3
        n1 = 8
    else:
        n1 = 0
    if (n[1] == '1'):#2^2
        n2 = 4
    else:
        n2 = 0
    if (n[2] == '1'):#2^1
        n3 = 2
    else:
        n3 = 0
    if (n[3] == '1'):#2^0
        n4 = 1
    else:
        n4 = 0
    dec = n1 + n2 + n3 + n4#Suma todos los valores
    # Mostrar resultados
    print("\nTu numero convertido a decimal es " + str(dec))

else:
    print("El úmero ingresado no es de 4 bits, por favor reinicia el programa")

