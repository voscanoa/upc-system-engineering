"""El cambio de moneda en la bolsa de Madrid el día 25 de agosto de 1987 fue el siguiente:

100 chelines austríacos = 956,871 pesetas
1 dólar americano       = 122,499 pesetas
100 dracmas griegas     = 88,607 pesetas
100 francos belgas      = 323,728 pesetas
1 franco francés        = 20,110 pesetas
1 libra esterlina       = 178,938 pesetas
100 liras italianas     = 9,289 pesetas"""

# Entrada
print("Monedas disponibles:")
print("1. chelin austriaco")
print("2. dolar americano")
print("3. dracma griego")
print("4. franco belga")
print("5. franco frances")
print("6. libra esterlina")
print("7. lira italiana")

opcion = int(input("Seleccione la moneda (1-7): "))
cantidad = float(input("Ingrese la cantidad de moneda: "))

# Inicialización
pesetas = 0

# Condicionales según la moneda
if opcion == 1:
    # 100 chelines = 956.871 pesetas
    pesetas = (cantidad * 956.871) / 100

elif opcion == 2:
    # 1 dólar = 122.499 pesetas
    pesetas = cantidad * 122.499

elif opcion == 3:
    # 100 dracmas = 88.607 pesetas
    pesetas = (cantidad * 88.607) / 100

elif opcion == 4:
    # 100 francos belgas = 323.728 pesetas
    pesetas = (cantidad * 323.728) / 100

elif opcion == 5:
    # 1 franco francés = 20.110 pesetas
    pesetas = cantidad * 20.110

elif opcion == 6:
    # 1 libra esterlina = 178.938 pesetas
    pesetas = cantidad * 178.938

elif opcion == 7:
    # 100 liras italianas = 9.289 pesetas
    pesetas = (cantidad * 9.289) / 100

else:
    print("Opción no válida")

# Salida
if opcion >= 1 and opcion <= 7:
    print("Equivalente en pesetas:", pesetas)
