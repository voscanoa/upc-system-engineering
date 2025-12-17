"""Escriba un algoritmo que muestre el nombre del día para una entrada entre 1 y 7."""

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia = int(input("Ingrese un número del 1 al 7: "))

if 1 <= dia <= 7:
    print(dias[dia - 1])
else:
    print("Número inválido")
