"""Encontrar la hipotenusa de un triángulo rectángulo conociendo sus dos catetos. Use el teorema de Pitágoras."""

from math import sqrt

ca = float(input("Ingrese el valor de tu cateto adyacente (CA): "))
co = float(input("Ingrese el valor de tu cateto opuesto (CO): "))

hipotenusa = sqrt((ca**2) + (co**2))

print("La hipotenusa es:", hipotenusa)
