"""Dado un triángulo de lados a,b y c, donde a > c y a > b. Determine el tipo de triángulo de acuerdo a las siguientes condiciones :
Si a2 = b2 + c2 => b es un triángulo rectángulo
Si a2 < b2 + c2 => b es un triángulo acutángulo
Si a2 > b2 + c2 => b es un triángulo obtusángulo"""

# Entrada
a = float(input("Ingrese el lado a (mayor): "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

# Validación básica del triángulo
if a <= 0 or b <= 0 or c <= 0:
    print("Los lados deben ser positivos")

elif a >= b + c:
    print("Los lados no forman un triángulo")

else:
    # Comparación de cuadrados
    a2 = a**2
    bc2 = b**2 + c**2

    if a2 == bc2:
        print("Es un triángulo rectángulo")

    elif a2 < bc2:
        print("Es un triángulo acutángulo")

    else:
        print("Es un triángulo obtusángulo")
