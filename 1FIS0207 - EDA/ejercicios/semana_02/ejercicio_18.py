"""Se desea convertir las calificaciones alfabéticas A, B, C, D o F a calificaciones numéricas 4, 5, 6 ,7 y 8 respectivamente."""

# Entrada
calificacion = input("Ingrese la calificación (A, B, C, D o F): ").upper()

# Condicionales
if calificacion == "A":
    numero = 4
elif calificacion == "B":
    numero = 5
elif calificacion == "C":
    numero = 6
elif calificacion == "D":
    numero = 7
elif calificacion == "F":
    numero = 8
else:
    print("Calificación no válida")
    numero = None

# Salida
if numero is not None:
    print("Calificación numérica:", numero)
