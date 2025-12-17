"""Se conoce el peso actual de una persona (en kilogramos), las calorías que quema por día, el peso objetivo y las calorías ingeridas por día por esa persona. Calcule el número de días que tardará la persona en alcanzar su objetivo. Considere la relación: 3500 calorías = 1 libra."""

# Datos de entrada
peso_actual = float(input("Ingrese el peso actual (kg): "))
peso_objetivo = float(input("Ingrese el peso objetivo (kg): "))
calorias_quemadas = float(input("Calorías quemadas por día: "))
calorias_ingeridas = float(input("Calorías ingeridas por día: "))

# Constantes
LIBRAS_POR_KG = 2.20462
CALORIAS_POR_LIBRA = 3500

# Cálculo del balance diario
balance_diario = calorias_quemadas - calorias_ingeridas

# Condicionales
if peso_actual == peso_objetivo:
    print("Ya se encuentra en el peso objetivo.")

elif balance_diario == 0:
    print("No alcanzará el peso objetivo porque no hay déficit ni superávit calórico.")

else:
    # Cambio de peso necesario
    cambio_peso_kg = abs(peso_actual - peso_objetivo)
    cambio_peso_libras = cambio_peso_kg * LIBRAS_POR_KG

    # Calorías necesarias
    calorias_necesarias = cambio_peso_libras * CALORIAS_POR_LIBRA

    # Verificar coherencia del objetivo
    if peso_actual > peso_objetivo and balance_diario > 0:
        dias = calorias_necesarias / balance_diario
        print("Días necesarios para bajar de peso:", round(dias))

    elif peso_actual < peso_objetivo and balance_diario < 0:
        dias = calorias_necesarias / abs(balance_diario)
        print("Días necesarios para subir de peso:", round(dias))

    else:
        print("Con esos datos no se puede alcanzar el peso objetivo.")
