"""Determine el grado de un acero bajo las siguientes condiciones: el acero se considera de grado 1 si T1 excede a 0.95 y T2 excede a 0.75; de grado 2 si T1 excede a 0.95 pero T2 no excede a 0.75; y de grado 3 si T1 no es mayor que 0.95"""

t1 = float(input("Ingrese el valor T1: "))
t2 = float(input("Ingrese el valor T2: "))

if t1 > 0.95:
    if t2 > 0.75:
        print("Grado 1")
    else:
        print("Grado 2")
else:
    print("Grado 3")
