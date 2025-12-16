"""Calcule la cantidad adeudada por un cliente de una compañía, considerando que la deuda actual es 15% más que la anterior. Tiene como dato la deuda anterior."""

deuda_anterior = 1000
incremento = 0.15

deuda_actual = deuda_anterior * (1 + incremento)

print(f"Tu deuda actual es: {deuda_actual:.2f}")
