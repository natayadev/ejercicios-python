from math import sqrt

usuario = input("Por favor, ingrese su nombre: ")
opcion = int(input(f"Hola {usuario}, ¿Qué desea hacer? Opciones: restar 1, sumar 2, multiplicar 3, calcular raiz cuadrada 4... "))

def raiz_cuadrada():
    valor = float(input("Debe ingresar un número entero o flotante a continuación: ")) 
    raiz_cuadrada = sqrt(valor)
    print(f"{usuario}, la raíz cuadrada es: ", raiz_cuadrada)

    #import math
    #help(math)

    print("Explorando la función sqrt")
    print(sqrt.__doc__)

def sumar():
    numero1 = float(input("Ingrese el primer número a continuación: "))
    numero2 = float(input("Ahora ingrese el segundo número: "))

    resultado = numero1 + numero2
    print(f"La suma es: {resultado}")

def restar():
    numero1 = float(input("Ingrese el primer número a continuación: "))
    numero2 = float(input("Ahora ingrese el segundo número: "))

    resultado = numero1 - numero2
    print(f"La resta es: {resultado}")

def multiplicar():
    numero1 = float(input("Ingrese el primer número a continuación: "))
    numero2 = float(input("Ahora ingrese el segundo número: "))

    resultado = numero1 * numero2
    print(f"El producto es: {resultado}")

if opcion == 1:
    restar()
elif opcion == 2:
    sumar()
elif opcion == 3:
    multiplicar()
elif opcion == 4:
    raiz_cuadrada()
else:
    print("Error, ingrese un número entero entre 1 y 4.")