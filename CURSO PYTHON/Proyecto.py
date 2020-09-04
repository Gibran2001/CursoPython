'''
PROYECTO FINAL
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")

#MENSAJES INICIALES
print("\t\t\tEste programa es un indicador de semáforo para el COVID-19\n\n")

#PROCESO PREVIO AL REGISTRO DE INDIVIDUOS
lista=[]#Aqui se guardan los datos
reg="Edad del individuo"+", "+"Indicador\n"#Mensaje inicial de la tabla
#Lo agrega para que al ver la tabla, pueda saber qu[e datos hay en la misma
lista.append(reg)
a=open("db.csv","a")
a.writelines(lista)
a.close()

#FUNCIONES SECUNDARIAS
def guardar(x,e,i):#Función para guardar en el archivo
    reg=str(e)+", "+str(i)+"\n"
    lista.append(reg)
    a=open("db.csv","a")
    a.writelines(lista[x])
    a.close()
def Sem(a):#Funcion para sacar el color del semaforo
    if(a==0):
        color="Verde"
        return color
    elif((a>1)and(a<31)):
        color="Amarillo"
        return color
    elif((a>30)and(a<71)):
        color="Naranja"
        return color
    elif(a>70):
        color="Rojo"
        return color

#PROCESO GENERAL
i=0#Este contador es el que registra los usuarios registrados
contagiados=0#Acumulador de contagiados
sumaEdades=0#Acumulador de las edades de los contagiados

#El ciclo termina cuando hay 100 individuos registrados
while(i<100):
    op=0#Menú
    while(op!=2):
        print("\n\n1.Registrar individuo (Máximo 100)\n2.Ver resultados parciales")
        op=int(input(f"Selecciona la operaión que deseas realizar ({i} usuarios registrados): "))
        if(op==1):
            edad=int(input("\nIngresa la edad del individuo: "))
            if(edad<0):#En caso de que introduzca una edad negativa
                print("Edad no válida, por favor intenta nuevaente")
            else:
                #Aumenta el contador de registrados
                i=i+1
                ind=float(input("Introduzca el indicador (0-1): "))
                if((ind<0)or(ind>1)):
                    print("Número inválido, por favor introduce un número entre 0 y 1")
                    i=i-1#Regresa el contador
                # En caso de que esté contagiado, suma a los acumuladores, si no es el caso no hace nada
                elif(ind>=0.8):
                    contagiados=contagiados+1
                    sumaEdades=sumaEdades
                    #Lo guarda en el archivo
                    guardar(i,edad,ind)
                else:#De no estar contagiado
                    #Lo guarda en el archivo
                    guardar(i,edad,ind)
                op=2#Para que salga del menú y vuelva a evaluar la condición de los registrados
        elif(op==2):
            print("\nEn un momento te mostraremos los resultados hasta ahora")
            if(len(lista)==0):
                print("\nNo tenemos usuarios registrados")
            else:
                print(f"\nHasta ahora tenemos {i} registrados")
                print(f"\nDe los cuales hay {contagiados} contagiados")
                sem=Sem(contagiados)
                print("\nEl semaforo indica que hasta ahora el color que corresponde es: "+str(sem))
                if(contagiados!=0):
                    prom=sumaEdades/contagiados
                    print("La tendencia indica que el promedio de edad de los contagiados es: "+str(prom))
        else:
            print("\nOpcion incorrecta, por favor vuelve a intentar\n")
#Una vez que salga del ciclo de los 100 numeros
print("\nSe han registrado a 100 individuos")
print(f"\nDe los cuales hay {contagiados} contagiados")
sem=Sem(contagiados)
print("\nEl semaforo indica que hasta ahora el color que corresponde es: "+str(sem))
if(contagiados!=0):
    prom=sumaEdades/contagiados
    print("El promedio de edad de los contagiados es: "+str(prom))
op=input("Si quieres ver la tabla con los datos presiona (s): ")
if((op=='s')or(op=='S')):#Reutilizamos variable
    a=open("db.csv","r")
    cont=a.read()
    a.close()
    print("\n"+cont)
else:
    print("De igual forma, puedes encontrar los datos en el archivo ""db.csv"" ")
print("Fin del programa, gracias por su preferencia")