"""Un distribuidor de material eléctrico vende alambre en rollos de 500, 300 y 75 pies.
Describa un algoritmo que pida al usuario una longitud total de alambres en pies que se requiere y envíe como salida el número de rollos de alambre de 500, 300 y 75 pies y el número de pies que faltan para completar el último rollo."""

# Entrada
pies = int(input("Ingrese la longitud total requerida (en pies): "))

# Inicialización
rollos_500 = 0
rollos_300 = 0
rollos_75 = 0

resto = pies

# Rollos de 500 pies
rollos_500 = resto // 500
resto = resto % 500

# Rollos de 300 pies
if resto >= 300:
    rollos_300 = resto // 300
    resto = resto % 300
else:
    rollos_300 = 0

# Rollos de 75 pies
if resto >= 75:
    rollos_75 = resto // 75
    resto = resto % 75
else:
    rollos_75 = 0

# Pies que faltan para completar el último rollo
if resto > 0:
    faltan = 75 - resto
else:
    faltan = 0

# Salida
print("Rollos de 500 pies:", rollos_500)
print("Rollos de 300 pies:", rollos_300)
print("Rollos de 75 pies:", rollos_75)
print("Pies que faltan para completar el último rollo:", faltan)
