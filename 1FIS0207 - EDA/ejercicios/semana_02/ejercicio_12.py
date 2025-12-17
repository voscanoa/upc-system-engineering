"""Un barril contendrá 11 monos, una jaula contendrá 7 monos y un coco contendrá un mono. Describa un algoritmo para solicitar una cantidad de monos con el fin de minimizar el número de contenedores usados."""

# Entrada
monos = int(input("Ingrese la cantidad de monos: "))

# Inicialización
barriles = 0
jaulas = 0
cocos = 0

# Barriles (11 monos)
barriles = monos // 11
resto = monos % 11

# Jaulas (7 monos)
if resto >= 7:
    jaulas = 1
    resto = resto - 7
else:
    jaulas = 0

# Cocos (1 mono)
if resto > 0:
    cocos = resto
else:
    cocos = 0

# Salida
print("Barriles:", barriles)
print("Jaulas:", jaulas)
print("Cocos:", cocos)
print("Total de contenedores:", barriles + jaulas + cocos)
