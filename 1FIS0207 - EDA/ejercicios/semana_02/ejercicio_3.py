"""Desarrolle un algoritmo para obtener el sueldo de los empleados, conociendo su pago por hora y el número de horas trabajadas en el mes. Para calcular el sueldo, use el factor “una vez y media” para las horas adicionales a las 40 horas."""

pago_hora = float(input("Ingrese el pago por hora: "))
horas_trabajadas = float(input("Ingrese las horas trabjadas: "))

horas_extra = horas_trabajadas - 40

if pago_hora < 40:
    sueldo = horas_trabajadas * pago_hora
else:
    sueldo = (40 * pago_hora) + (horas_extra * pago_hora * 1.5)

print(f"El sueldo a recibir es de: S/.{sueldo:.2f}")
print(f"Tienes {horas_extra} horas extras")
