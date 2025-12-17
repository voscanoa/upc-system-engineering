"""Determinar el monto a pagar por un alumno de un instituto cuya cuota tiene un porcentaje de descuento que se establece en la siguiente tabla y está en función al colegio de procedencia del alumno; así mismo los importes están exonerados de impuestos.

Colegio       A   B   C
Nacional     50  40  30
Particular   25  20  15"""

# Entrada de datos
cuota = float(input("Ingrese el monto de la cuota: "))
colegio = input("Ingrese el tipo de colegio (Nacional / Particular): ").lower()
categoria = input("Ingrese la categoría (A, B, C): ").upper()

# Determinar porcentaje de descuento
if colegio == "nacional":
    if categoria == "A":
        descuento_porcentaje = 50
    elif categoria == "B":
        descuento_porcentaje = 40
    elif categoria == "C":
        descuento_porcentaje = 30
    else:
        descuento_porcentaje = 0
        print("Categoría no válida.")
elif colegio == "particular":
    if categoria == "A":
        descuento_porcentaje = 25
    elif categoria == "B":
        descuento_porcentaje = 20
    elif categoria == "C":
        descuento_porcentaje = 15
    else:
        descuento_porcentaje = 0
        print("Categoría no válida.")
else:
    descuento_porcentaje = 0
    print("Tipo de colegio no válido.")

# Cálculos
descuento = cuota * descuento_porcentaje / 100
monto_pagar = cuota - descuento

# Mostrar resultados
print("\n--- DETALLE DE PAGO ---")
print(f"Cuota original: S/ {cuota:.2f}")
print(f"Descuento aplicado: {descuento_porcentaje}%")
print(f"Monto del descuento: S/ {descuento:.2f}")
print(f"Monto a pagar: S/ {monto_pagar:.2f}")
