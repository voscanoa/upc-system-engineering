"""
Dado el año de nacimiento de una persona calcule su edad
"""

from datetime import datetime


def edad(date):
    anio_actual = datetime.now().year
    return anio_actual - date


fecha_nacimiento = int(input("Ingrese su fecha de nacimiento: "))
edad_actual = edad(fecha_nacimiento)
print(f"tienes: {edad_actual} años")
