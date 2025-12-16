"""Calcular el monto a cobrar, incluyendo los impuestos, el impuesto sobre las ventas es 18% del importe de la venta."""

importe_venta = float(input("Muestre el importe de venta: "))

impuesto = importe_venta * 0.18
monto_cobrar = importe_venta + impuesto

print(f"El monto a cobrar es: {monto_cobrar:.2f}")
