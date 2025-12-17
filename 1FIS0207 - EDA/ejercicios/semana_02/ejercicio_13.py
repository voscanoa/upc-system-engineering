"""Encontrar la hipotenusa de un triángulo rectángulo conociendo sus dos catetos. Use el teorema de Pitágoras. Hipotenusa^2 = cateto1^2 + cateto2^2"""

import math

# Entrada de datos
cateto1 = float(input("Ingrese el primer cateto: "))
cateto2 = float(input("Ingrese el segundo cateto: "))

# Condicional para validar datos
if cateto1 <= 0 or cateto2 <= 0:
    print("Los catetos deben ser valores positivos.")
else:
    # Teorema de Pitágoras
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print("La hipotenusa es:", hipotenusa)
