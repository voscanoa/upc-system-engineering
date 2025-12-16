"""Si se conoce el número de horas trabajadas, el valor de la hora trabajada y la tasa del impuesto, calcule el pago bruto, el descuento que se aplicará por el impuesto, pago neto."""

"""
piden:
    - Numeros de horas
    - Valor de hora
    - Tasa de impuesto(%)

pago_bruto = horas_trabajadas * valor_hora
descuento = pago_bruto * tasa_impuesto
pago_neto = pago_bruto - descuento
"""

horas_trabajadas = float(input("Ingrese tus horas trabajadas: "))
valor_horas_trabajada = float(input("Ingrese el valor horas trabajadas: "))
tasa_impuesto = float(input("Ingrese la tasa de impuestos: "))

pago_bruto = horas_trabajadas * valor_horas_trabajada
descuento = pago_bruto * (tasa_impuesto / 100)
pago_neto = pago_bruto - descuento

print("\n")
print(f"El pago bruto equivale a: {pago_bruto}")
print(f"El descuento es: {descuento}")
print(f"El pago ento equivale a: {pago_neto}")
