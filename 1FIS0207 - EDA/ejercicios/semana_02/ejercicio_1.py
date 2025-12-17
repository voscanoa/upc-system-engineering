"""Dado un número mostrar mensaje de si es par o impar."""

numero = float(input("Ingrese numero: "))

tipo = "par" if numero % 2 == 0 else "Impar"

print(f"El número {numero} es {tipo}.")
