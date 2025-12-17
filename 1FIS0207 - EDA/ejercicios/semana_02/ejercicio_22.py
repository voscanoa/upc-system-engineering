"""Se lee el código del empleado, número de horas trabajadas, sueldo por hora. Calcular el pago neto considerando la siguiente tabla de descuento.

Sueldo bruto       | Descuento
------------------ | ----------
Menor 500          | 0
Entre 501 y 1000   | 2%
Entre 1001 y 4000  | 8%
Entre 4001 y 8000  | 15%
Entre 8001 y 10000 | 21%
Mayor 10001        | 30%
"""

# Entrada de datos
codigo = input("Ingrese el código del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
sueldo_hora = float(input("Ingrese el sueldo por hora: "))

# Cálculo del sueldo bruto
sueldo_bruto = horas_trabajadas * sueldo_hora

# Determinar porcentaje de descuento
if sueldo_bruto < 500:
    descuento_porcentaje = 0
elif sueldo_bruto <= 1000:
    descuento_porcentaje = 2
elif sueldo_bruto <= 4000:
    descuento_porcentaje = 8
elif sueldo_bruto <= 8000:
    descuento_porcentaje = 15
elif sueldo_bruto <= 10000:
    descuento_porcentaje = 21
else:
    descuento_porcentaje = 30

# Cálculo del descuento y sueldo neto
descuento = sueldo_bruto * descuento_porcentaje / 100
sueldo_neto = sueldo_bruto - descuento

# Mostrar resultados
print("\n--- BOLETA DE PAGO ---")
print(f"Código del empleado: {codigo}")
print(f"Sueldo bruto: S/ {sueldo_bruto:.2f}")
print(f"Descuento ({descuento_porcentaje}%): S/ {descuento:.2f}")
print(f"Pago neto: S/ {sueldo_neto:.2f}")
