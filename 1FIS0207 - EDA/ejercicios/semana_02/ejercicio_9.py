"""En una factura está registrada la cantidad de disquetes vendidos, considerando que se tienen cajas para embalar 6 disquetes, indique el número de cajas necesarias para embalar todos los disquetes vendidos. Ejemplo: 12 diskette → 2 cajas 15 diskette → 3 cajas"""

total_vendidos = int(input("Ingrese la cantidad vendidas: "))

una_caja = 6

total_cajas = total_vendidos // 6
if total_vendidos % 6 != 0:
    total_cajas = total_cajas + 1

print(f"El total de cajas a usar son: {total_cajas}")
