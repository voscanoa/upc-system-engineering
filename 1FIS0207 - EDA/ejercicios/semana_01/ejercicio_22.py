"""El personal de ventas de una empresa recibe S/.200.00 por semana más 9% de las ventas de esa semana. Si se tiene como dato las ventas de un vendedor en una semana calcule y muestre sus ganancias."""

ventas = float(input("Ingrese el monto de ventas de la semana: "))

sueldo_fijo = 200
comision = 0.09 * ventas

ganancia_total = sueldo_fijo + comision

print(f"Las ganancias del vendedor son: S/. {ganancia_total:.2f}")
