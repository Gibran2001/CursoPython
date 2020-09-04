'''
EJERCICIO 8
Programa hecho por Mauricio Gibrán Colima Flores
Curso de Introducción a Python
'''

#Importar librería para limpiar pantalla
import os
os.system("cls")
def Fact(a):#Funcion para sacar el factorial
    x = 1
    for i in range(1,a+1):
        x=x*i
    print("El factorial de tu numero es " + str(x))

#mensaje de bienvenida
print("\t\tCalculadora básica\n")

#Proceso
n=0
while(n!=8):
    print("1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Modulo\n6.Potencia\n7.Factorial\n8.Salir")
    n = int(input("Por favor escriba el número que corresponda a la operación que desea realizar: "))
    if(n==1):
        print("\n\nSuma")
        n1=int(input("\nIntroduce tu primer número: "))
        n2=int(input("\nnIntroduce tu segundo número: "))
        r=n1+n2
        print("El resultado de la suma es: "+str(r))
    elif(n==2):
        print("\n\nResta")
        n1=int(input("\nIntroduce tu primer número: "))
        n2=int(input("\nnIntroduce tu segundo número: "))
        r=n1-n2
        print("El resultado de la resta es: "+str(r))
    elif(n==3):
        print("\n\nMultiplicación")
        n1=int(input("\nIntroduce tu primer número: "))
        n2=int(input("\nnIntroduce tu segundo número: "))
        r=n1*n2
        print("El resultado de la multiplicación es: "+str(r))
    elif(n==4):
        print("\n\nDivisión")
        n1=int(input("\nIntroduce el divisor: "))
        n2=int(input("\nnIntroduce el dividendo: "))
        if(n2==0):
            print("No se puede realizar la división entre cero, por favor reinicia el programa")
        else:
            r=n1/n2
            print("El resultado de la resta es: " + str(r))
    elif(n==5):
        print("\n\nMódulo")
        n1=int(input("\nIntroduce el primer número: "))
        n2=int(input("\nnIntroduce el segundo número: "))
        r=n1%n2
        print("El residuo de tu primer número entre el segundo es: "+str(r))
    elif(n==6):
        print("\n\nPotencia")
        n1=int(input("\nIntroduce tu primer número: "))
        n2=int(input("\nnIntroduce el número al cual lo quieres elevar: "))
        r=n1**n2
        print("El resultado es: "+str(r))
    elif(n==7):
        print("\n\nFactorial")
        n1 = int(input("\nIntroduce tu número para sacar su factorial: "))
        Fact(n1)
    elif(n==8):
        print("Gracias por tu preferencia...")
    else:
        n=int(input("Opción incorrecta, por favor presiona 8: "))