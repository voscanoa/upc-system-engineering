"""Dada la edad de una persona en meses, calcule su edad en años y fracción de meses."""

edad_meses = int(input("Ingrese la cantidad de meses: "))

años = edad_meses // 12
meses = edad_meses % 12

print(f"La edad es {años} años y {meses} meses.")
