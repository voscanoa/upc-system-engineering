"""18. Calcular el área de un triángulo, conociendo dos lados y el ángulo (en grados sexagesimales) entre ellos.
Aplique la fórmula:
Area = (Lado1 . Lado2 . Sen(Angulo))/2
donde el ángulo debe estar expresado en Radianes.
Nota Para convertir un ángulo sexagesimal a radianes, aplique la fórmula:
Angulo Radianes = (PI . Angulo sexagesimales)/180
 180
"""

import math

lado_1 = float(input("Ingrese el lado 1: "))
lado_2 = float(input("Ingrese el lado 2: "))
angulo = float(input("Ingrese el angualo en sexagesimales: "))

angulo_radian = math.pi * angulo / 180
area = lado_1 * lado_2 * math.sin(angulo)

print(f"El area del triangulo es: {area:.2f}")
