"""Resolver una ecuación de segundo grado, teniendo como entrada los valores a, b y c"""

import cmath


def ecuacion_cuadratica(a, b, c):
    """
    Resuelve la ecuación cuadrática ax^2 + bx + c = 0.

    Args:
        a (float): Coeficiente de x^2
        b (float): Coeficiente de x
        c (float): Término constante

    Returns:
        Dos soluciones (reales o complejas)
    """
    if a == 0:
        raise ValueError(
            "El coeficiente 'a' no puede ser cero en una ecuación cuadrática."
        )

    delta = b**2 - 4 * a * c
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    return x1, x2


def main():
    try:
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))

        x1, x2 = ecuacion_cuadratica(a, b, c)

        print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
