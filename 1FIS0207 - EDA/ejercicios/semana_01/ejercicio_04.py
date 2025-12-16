"""Obtenga la edad de una persona en meses, dada su edad en años y meses."""

edad_anios = int(input("Ingresa tu edad actual: "))
edad_meses = int(input("Ingresa ls meses: "))

total_meses = (edad_anios * 12) + edad_meses

print("La edad total en meses es:", total_meses)
