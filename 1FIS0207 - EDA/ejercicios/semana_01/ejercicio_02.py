"""
Desarrolle un algoritmo que realice la suma, resta, multiplicación, división y modulo
"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return a % b


def validar_numero(texto: str):
    try:
        return float(texto)
    except ValueError:
        raise ValueError(f"'{texto}' no es un número válido")


def mostrar_menu() -> None:
    print("  1. Suma (+)")
    print("  2. Resta (-)")
    print("  3. Multiplicación (*)")
    print("  4. División (/)")
    print("  5. Módulo (%)")
    print("  0. Salir")


def realizar_operacion(opcion, num1, num2):
    operaciones = {
        "1": (suma, "+"),
        "2": (resta, "-"),
        "3": (multiplicacion, "*"),
        "4": (dividir, "/"),
        "5": (modulo, "%"),
    }
    if opcion not in operaciones:
        return None

    funcion, simbolo = operaciones[opcion]
    resultado = funcion(num1, num2)

    print(f"Resultado: {num1} {simbolo} {num2} = {resultado}")

    return resultado


def main():
    while True:
        try:
            mostrar_menu()
            opcion = input("\nSeleccione una operación (0-6): ").strip()

            if opcion == "0":
                print("\n¡Gracias por usar la calculadora! Hasta pronto.\n")
                break

            if opcion not in ["1", "2", "3", "4", "5", "6"]:
                print("\n✗ Error: Opción no válida. Por favor seleccione 0-6.")
                continue

            # Solicitar los números
            num1_input = input("\nIngrese el primer número: ").strip()
            num1 = validar_numero(num1_input)

            num2_input = input("Ingrese el segundo número: ").strip()
            num2 = validar_numero(num2_input)

            # Realizar la operación
            realizar_operacion(opcion, num1, num2)

            # Preguntar si desea continuar
            continuar = (
                input("\n¿Desea realizar otra operación? (s/n): ").lower().strip()
            )
            if continuar != "s":
                print("\n¡Gracias por usar la calculadora! Hasta pronto.\n")
                break

        except ValueError as e:
            print(f"\n✗ Error: {e}")
            print("Por favor, intente nuevamente.")

        except ZeroDivisionError as e:
            print(f"\n✗ Error matemático: {e}")
            print("Por favor, intente con otros números.")

        except KeyboardInterrupt:
            print("\n\nPrograma cancelado por el usuario.")
            print("¡Hasta pronto!\n")
            break

        except Exception as e:
            print(f"\n✗ Error inesperado: {e}")
            print("Por favor, intente nuevamente.")


if __name__ == "__main__":
    main()
