import os
import time
import math
os.system("color a")


def soma():
    numero=input("escreva um número: ")
    numero2=input("escreva outro número: ")
    resultado= int(numero) + int(numero2)
    print("o resultado da soma é:  ",resultado)


def substracao():
    numero=input("escreva um número: ")
    numero2=input("escreva outro número: ")
    resultado= int(numero) - int(numero2)
    print("o resultado da subtracão é:  ",resultado)


def multiplicacao():
    numero=input("escreva um número: ")
    numero2=input("escreva outro número: ")
    resultado= int(numero) * int(numero2)
    print("o resultado da multiplicação é:  ",resultado)



def divisao():
    numero=input("escreva um número: ")
    numero2=input("escreva outro número: ")
    resultado= int(numero) / int(numero2)
    print("o resultado da divisão é:  ",resultado)



def potencia():
    numero=input("escreva um número: ")
    numero2=input("escreva outro número: ")
    resultado= int(numero) ** int(numero2)
    print("o resultado da potência é:  ",resultado)



def raiz_quadrada():
    numero=input("escreva um número: ")
    resultado= math.sqrt(int(numero))
    print("o resultado da raiz quadrada é:  ",resultado)









running=True

while running:
    os.system("cls")
    print("para soma digite 1: ")
    print("para subtração digite 2: ")
    print("para multiplicação digite 3: ")
    print("para divisão digite 4: ")
    print("para potência digite 5: ")
    print("para raiz quadrada digite 6:  ")
    valor=input("")



    if valor=="1":
        soma()
    elif valor=="2":
        substracao()
    elif valor=="3":
        multiplicacao()
    elif valor=="4":
        divisao()
    elif valor=="5":
        potencia()
    elif valor=="6":
        raiz_quadrada()
    else:
        print("tente novamente")

    time.sleep(3)