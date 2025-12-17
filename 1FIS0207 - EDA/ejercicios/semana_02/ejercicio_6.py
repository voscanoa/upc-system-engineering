"""El valor de y se define como sigue:
Y = x^2 +2x - 3 si  -3 <= x <= 2
Y = 5x + 7      si  2 < x <= 10
Y = 0           si  x <= -3 o x > 10
"""

valor_x = float(input("Ingrese el valor de 'x': "))
if -3 <= valor_x <= 2:
    Y = valor_x**2 + 2 * valor_x - 3
elif 2 < valor_x <= 10:
    Y = 5 * valor_x + 7
else:
    Y = 0

print(f"El valor de y es: {Y}")
