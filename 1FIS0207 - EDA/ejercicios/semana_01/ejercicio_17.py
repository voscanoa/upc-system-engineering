"""Determinar la suma de los N primeros números enteros de acuerdo a la siguiente fórmula:
Suma = N(N+1)/2"""

numero = int(input("Ingrese cantidad de numero N: "))
suma = numero * (numero + 1) / 2

print(f"La suma de los primeros {numero} numeros es: {suma}")
