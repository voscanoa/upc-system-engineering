"""Para un valor de hora dado en el formato: HH, MM, SS . Calcula la hora que será dentro de un minuto."""

# Entrada
hh = int(input("Ingrese la hora (HH): "))
mm = int(input("Ingrese los minutos (MM): "))
ss = int(input("Ingrese los segundos (SS): "))

# Validación básica
if hh < 0 or hh > 23 or mm < 0 or mm > 59 or ss < 0 or ss > 59:
    print("Hora no válida")
else:
    # Sumar un minuto
    mm = mm + 1

    # Condicionales para ajustar la hora
    if mm == 60:
        mm = 0
        hh = hh + 1

        if hh == 24:
            hh = 0

    # Salida
    print("Hora dentro de un minuto:")
    print(f"{hh:02d}:{mm:02d}:{ss:02d}")
