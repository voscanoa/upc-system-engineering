"""Para un par de números calcule el residuo resultante de dividir el numero mayor entre el numero menor. 21%4 22%6 5%8"""

num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))

# Validación básica
if num1 == 0 or num2 == 0:
    print("No se puede dividir entre cero.")
else:
    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1

    residuo = mayor % menor

print(f"El residuo de dividir {mayor} entre {menor} es: {residuo}")
