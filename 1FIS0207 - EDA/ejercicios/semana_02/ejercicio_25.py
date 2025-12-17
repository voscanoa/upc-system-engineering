"""Construir un programa que calcule el índice de masa corporal de una persona
(IMC = peso [kg] / altura2 [m]) e indique el estado en el que se encuentra esa
persona en función del valor de IMC:
valor de IMC Diagnóstico
< 16 Criterio de ingreso en hospital
de 16 a 17 infrapeso
de 17 a 18 bajo peso
de 18 a 25 peso normal (saludable)
de 25 a 30 sobrepeso (obesidad de grado I)
de 30 a 35 sobrepeso crónico (obesidad de grado II)
de 35 a 40 obesidad premórbida (obesidad de grado III)
>40 obesidad mórbida (obesidad de grado IV)
Nota 1: se recomienda el empleo de sentencias si, cuando"""

# Entrada de datos
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Cálculo del IMC
imc = peso / (altura**2)

# Mostrar IMC
print(f"\nSu IMC es: {imc:.2f}")

# Evaluación del diagnóstico
if imc < 16:
    print("Diagnóstico: Criterio de ingreso en hospital")
elif imc >= 16 and imc < 17:
    print("Diagnóstico: Infrapeso")
elif imc >= 17 and imc < 18:
    print("Diagnóstico: Bajo peso")
elif imc >= 18 and imc < 25:
    print("Diagnóstico: Peso normal (saludable)")
elif imc >= 25 and imc < 30:
    print("Diagnóstico: Sobrepeso (Obesidad grado I)")
elif imc >= 30 and imc < 35:
    print("Diagnóstico: Sobrepeso crónico (Obesidad grado II)")
elif imc >= 35 and imc < 40:
    print("Diagnóstico: Obesidad premórbida (Obesidad grado III)")
else:
    print("Diagnóstico: Obesidad mórbida (Obesidad grado IV)")
