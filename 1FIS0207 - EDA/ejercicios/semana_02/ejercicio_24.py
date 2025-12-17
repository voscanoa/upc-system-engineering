"""En una tienda de accesorios para computadoras, el precio de venta unitario de los disquetes es el mismo para cualquier marca, sin embargo el descuento varía de acuerdo a la marca y se establece en la siguiente tabla. Determinar el importe a pagar por la cantidad de disquetes comprados de una sola marca, considerando que no se paga impuestos. Mostrar importe bruto, descuento e importe a pagar.

Marca     Dscto(%)
 3M         10
 NCR        15
Sentinel    20
Burroughs   25
Goldstar    30
"""

# Entrada de datos
precio_unitario = float(input("Ingrese el precio unitario del disquete: "))
cantidad = int(input("Ingrese la cantidad de disquetes: "))
marca = input("Ingrese la marca (3M, NCR, Sentinel, Burroughs, Goldstar): ").lower()

# Cálculo del importe bruto
importe_bruto = precio_unitario * cantidad

# Determinar descuento según la marca
if marca == "3m":
    descuento_porcentaje = 10
elif marca == "ncr":
    descuento_porcentaje = 15
elif marca == "sentinel":
    descuento_porcentaje = 20
elif marca == "burroughs":
    descuento_porcentaje = 25
elif marca == "goldstar":
    descuento_porcentaje = 30
else:
    descuento_porcentaje = 0
    print("Marca no válida, no se aplicará descuento.")

# Cálculo del descuento y total a pagar
descuento = importe_bruto * descuento_porcentaje / 100
importe_pagar = importe_bruto - descuento

# Mostrar resultados
print("\n--- RESUMEN DE COMPRA ---")
print(f"Importe bruto: S/ {importe_bruto:.2f}")
print(f"Descuento ({descuento_porcentaje}%): S/ {descuento:.2f}")
print(f"Importe a pagar: S/ {importe_pagar:.2f}")
