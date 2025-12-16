"""Hallar el área lateral, área total y volumen de un cilindro. Aplique las fórmulas a seguir:
- Area lateral = 2 pi Radio * Altura
- Area total = Area lateral * 2 área de la base
- Volumen = pi Radio^2*Altura
"""

import math

radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))

PI = math.pi
area_lateral = 2 * PI * radio * altura
area_base = PI * radio**2
area_total = area_lateral + 2 * area_base
volumen = PI * radio**2 * altura

print(f"El area lateral es {area_lateral:.2f}")
print(f"El area base es {area_base:.2f}")
print(f"El area total es {area_total:.2f}")
print(f"El volumen es {volumen:.2f}")
