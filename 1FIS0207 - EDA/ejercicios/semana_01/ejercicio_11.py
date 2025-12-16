"""La energía eléctrica, en watts, de un circuito de corriente directa (cd) se define como el producto de voltaje y corriente: E = V C
    - E energía en watts
    - V voltaje en voltios
    - C corriente en amperios
Escriba un algoritmo para encontrar la energía de corriente directa, voltaje y la corriente, conociendo los otros dos valores."""

print("¿Qué desea calcular?")
print("1. Energía (E)")
print("2. Voltaje (V)")
print("3. Corriente (C)")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    voltaje = float(input("Ingrese el voltaje (V): "))
    corriente = float(input("Ingrese la corriente (C): "))
    energia = voltaje * corriente
    print("La energía es:", energia, "watts")

elif opcion == 2:
    energia = float(input("Ingrese la energía (E): "))
    corriente = float(input("Ingrese la corriente (C): "))
    voltaje = energia / corriente
    print("El voltaje es:", voltaje, "voltios")

elif opcion == 3:
    energia = float(input("Ingrese la energía (E): "))
    voltaje = float(input("Ingrese el voltaje (V): "))
    corriente = energia / voltaje
    print("La corriente es:", corriente, "amperios")

else:
    print("Opción no válida")
