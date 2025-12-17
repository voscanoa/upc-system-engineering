"""Se tiene la siguiente información:

Figura geométrica   Dimension1    Dimension2
Rectángulo          Largo         Ancho
Triángulo           Largo         Ancho
Cuadrado            Lado          No usado
Círculo             Radio         No usado

Teniendo el tipo de figura y las dimensiones correspondientes calcular el área de la figura geométrica."""

import math

# Entrada
figura = input("Ingrese la figura (rectangulo, triangulo, cuadrado, circulo): ").lower()

# Condicionales según la figura
if figura == "rectangulo":
    largo = float(input("Ingrese el largo: "))
    ancho = float(input("Ingrese el ancho: "))
    area = largo * ancho
    print("Área del rectángulo:", area)

elif figura == "triangulo":
    largo = float(input("Ingrese el largo: "))
    ancho = float(input("Ingrese el ancho: "))
    area = (largo * ancho) / 2
    print("Área del triángulo:", area)

elif figura == "cuadrado":
    lado = float(input("Ingrese el lado: "))
    area = lado**2
    print("Área del cuadrado:", area)

elif figura == "circulo":
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio**2
    print("Área del círculo:", area)

else:
    print("Figura geométrica no válida.")
