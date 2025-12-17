"""Calcular el total a pagar considerando: que el impuesto de venta es del 6% en cualquier compra de 500 nuevos soles o menos, pero sólo del 3.5% en una compra superior a los 500 nuevos soles. Si el impuesto es mayor a 550 nuevos soles se deberá sumar al impuesto una multa del 6%."""

# Entrada
compra = float(input("Ingrese el monto de la compra (S/): "))

# Inicialización
impuesto = 0
multa = 0

# Cálculo del impuesto según el monto de compra
if compra <= 500:
    impuesto = compra * 0.06
else:
    impuesto = compra * 0.035

# Condicional para la multa
if impuesto > 550:
    multa = impuesto * 0.06

# Total a pagar
total = compra + impuesto + multa

# Salida
print("Monto de la compra: S/", compra)
print("Impuesto: S/", impuesto)
print("Multa: S/", multa)
print("Total a pagar: S/", total)
