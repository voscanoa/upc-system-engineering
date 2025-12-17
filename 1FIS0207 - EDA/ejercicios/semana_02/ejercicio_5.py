"""El interés que se carga a una cuenta de tarjeta de crédito depende del saldo a pagar de acuerdo con el siguiente criterio: el interés cargado es 18% para saldos de hasta $500 y del 20% para saldos mayores a $500. Desarrolle un algoritmo para encontrar la cantidad total de interés de acuerdo al saldo de una cuenta."""

saldo = float(input("Ingrese el saldo de la cuenta: "))

tasa = 0.18 if saldo <= 500 else 0.20
interes = tasa * saldo

print(f"Interés aplicado: {interes:.2f}")
