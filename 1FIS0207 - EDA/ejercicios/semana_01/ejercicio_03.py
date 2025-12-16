"""
Calculadora de ecuación polinomial.
Calcula Y = (2X - 7X)(X + 2)(X - 6)
"""


def calcular_ecuacion(x):
    termino1 = 2 * x - 7 * x  # Equivale a -5X
    termino2 = x + 2
    termino3 = x - 6

    return termino1 * termino2 * termino3


def validar_numero(texto):
    """
    Valida y convierte una entrada de texto a número.

    Args:
        texto: String a convertir

    Returns:
        Número float validado

    Raises:
        ValueError: Si el texto no es un número válido
    """
    try:
        return float(texto)
    except ValueError:
        raise ValueError(f"'{texto}' no es un número válido")


def main():
    x_input = input("\nIngrese el valor de X: ").strip()
    x = validar_numero(x_input)
    y = calcular_ecuacion(x)
    print(f"El valor de Y es: {y}")


if __name__ == "__main__":
    main()
