"""Una tienda muestra el precio de venta de sus productos (incluye el IGV).
Determinar el IGV y el valor de venta del producto"""

precio_final = float(input("Muestre el precio de venta: "))

valor_venta = precio_final / 1.18
IGV = precio_final - valor_venta

print(f"Valor de venta es: {valor_venta:.2f}")
print(f"IGV: {IGV:.2f}")
