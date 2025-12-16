"""Escriba un algoritmo que permita al usuario convertir entre las siguientes unidades:
    - Grados fahrenheit a grados centígrados
    - Grados centígrados a grados fahrenheit
    - Pulgadas a centímetros
    - Centímetros a pulgadas
    - Libras a kilogramos
    - Kilogramos a libras
1 Kg = 2.204 Lb"""

print("¿Qué desea calcular?")
print("1. Grados fahrenheit a grados centígrados")
print("2. Grados centígrados a grados fahrenheit")
print("3. Pulgadas a centímetros")
print("4. Centímetros a pulgadas")
print("5. Libras a kilogramos")
print("6. Kilogramos a libras")

opcion = int(input("Seleccione una opcion: "))

match opcion:
    case 1:
        fahrenheit = float(input("Ingrese Grados fahrenheit: "))
        centigrados = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} F° <> {centigrados:.2f} C°")
    case 2:
        centigrados = float(input("Ingrese Grados centigrados: "))
        fahrenheit = (centigrados * 9 / 5) + 32
        print(f"{centigrados} C° <> {fahrenheit:.2f} F°")
    case 3:
        pulgadas = float(input("Ingrese la cantidad en pulgadas: "))
        centimetros = pulgadas * 2.54
        print(f"{pulgadas} inch <> {centimetros:.2f} cm")
    case 4:
        centimetros = float(input("Ingrese la cantidad en centimetros: "))
        pulgadas = centimetros / 2.54
        print(f"{centimetros} cm <> {pulgadas:.2f} inch")
    case 5:
        libras = float(input("Ingrese la cantidad en libras: "))
        kilogramos = libras * 0.453592
        print(f"{libras} lib <> {kilogramos:.2f} kg")
    case 6:
        kilogramos = float(input("Ingrese la cantidad en kilogramos: "))
        libras = kilogramos * 2.20462
        print(f"{kilogramos} kg <> {libras:.2f} lib")
    case 7:
        print("Opcion no valida")
