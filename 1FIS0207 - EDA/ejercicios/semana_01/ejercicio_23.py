"""Con el valor del radio de un círculo, calcule el diámetro, la circunferencia y el área. Use el valor 3.14259 para la constante PI."""

radio = float(input("Ingrese el radio del círculo: "))

PI = 3.14259

diametro = 2 * radio
circunferencia = 2 * PI * radio
area = PI * radio**2

print(f"Diámetro: {diametro:.2f}")
print(f"Circunferencia: {circunferencia:.2f}")
print(f"Área: {area:.2f}")
