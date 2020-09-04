'''
EJERCICIO 9
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería
import os
os.system("cls")

#Mensajes iniciales
print("\t\t\tEste programa pide datos de alumnos y genera su promedio del grupo")

#Proceso
op=0
nAlmumnos=0
sumaCalf=0
lista=[]
while(op!=2):
    print("1.Agregar alumno\n2.Salir y promediar")
    op=int(input("Presiona la opcion que quieres realizar: "))
    if(op==1):
        nAlmumnos=nAlmumnos+1
        nom=input("Introdice el nombre del alumno: ")
        calf=input("\nIntroduce su calificacion: ")
        sumaCalf=sumaCalf+int(calf)
        reg=nom+", "+calf+"\n"
        lista.append(reg)
    elif(op==2):
        if(nAlmumnos==0):
            print("No hay alumnos en este grupo")
        else:
            print("El grupo est[a conformado por: "+str(lista))
            prom=sumaCalf/nAlmumnos
            print("\n\nEl promedio del grupo es: "+str(prom))
    else:
        print("Opcion incorrecta... Reiniciando programa")