"""Conociendo que un automóvil parte del reposo con una aceleración constante A y que T representa el tiempo (en segundos). Calcular la distancia recorrida (D) y la velocidad final del automóvil (V).
D = 1/2 A*T^2  y V = A*T"""

A = float(input("Ingresa la aceleracion: "))
T = float(input("Ingresa el tiemp: "))

distancia_recorrida = 1 / 2 * A * T**2
velocidad_final = A * T

print(f"La distancia recorrida es: {distancia_recorrida} m")
print(f"La velocidad final es: {velocidad_final} m/s")
