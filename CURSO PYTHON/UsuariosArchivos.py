'''
EJERCICIO 10
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería
import os
os.system("cls")

#Mensajes iniciales
print("\t\t\tEste programa registra usuarios y contraseñas para guardarlas en un archivo\n\n")

#Proceso
lista=[]
op=0
while(op!=2):
    print("1.Registrar usuario\n2.Salir y mostrar usuarios registrados")
    op=int(input("\nELige una opción dentro del menú: "))
    if(op==1):
        usuario=input("\nIntroduce el nombre de usuario: ")
        contrasena=input("\nIntroduce tu contraseña (Debe de contener al menos 8 caracteres): ")
        if(len(contrasena)<8):
            print("\nTu contraseña no contiene los 8 caracteres, por favor intenta de nuevo")
        else:
            reg=usuario+", "+contrasena+"\n"
            lista.append(reg)
            a=open("usuarios.csv","a")
            a.writelines(lista)
            a.close()
    elif(op==2):
        if(len(lista)==0):
            print("No hay usuarios registrados")
        else:
            a=open("usuarios.csv","r")
            cont=a.read()
            a.close()
            print(cont)
    else:
        print("Opcion incorrecta")
