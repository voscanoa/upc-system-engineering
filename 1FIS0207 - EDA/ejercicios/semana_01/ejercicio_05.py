"""Dado el valor de venta de un producto, calcular el Impuesto General a las Ventas y el precio de venta."""

valor_venta = float(input("Ingrese el valor de venta: "))

impuesto = 0.18 * valor_venta
precio_venta = valor_venta + impuesto

print(f"Impuesto general es: {impuesto:.2f}")
print(f"Precio de venta: {precio_venta:.2f}")
