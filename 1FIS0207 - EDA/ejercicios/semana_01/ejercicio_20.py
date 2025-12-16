"""La nota final de un curso de programación se obtiene de acuerdo a las siguientes fórmulas:
    - PF = (Ep + 2Ef + Pp)/4
    - Ef = (2Pe + Py)/3
    - Pp = (2Pa + Pc)/3
    - PF : promedio final
    - Ep : examen parcial
    - Ef : Examen final
    - Pp : promedio de prácticas
    - Pe : prueba escrita del examen final
    - Py : proyecto
    - Pa : promedio de prácticas de aula
    - Pc : promedio de notas de concepto del profesor
Según reglamento, la nota mínima aprobatoria es 10.5 y los promedios parciales no se redondean. Un alumno sumamente preocupado, desea saber cuánto deberá sacar como nota en la prueba escrita del examen final para aprobar dicho curso si ya sabe las demás notas."""

# Entradas
Ep = float(input("Ingrese la nota del examen parcial (Ep): "))
Py = float(input("Ingrese la nota del proyecto (Py): "))
Pa = float(input("Ingrese el promedio de prácticas de aula (Pa): "))
Pc = float(input("Ingrese el promedio de concepto del profesor (Pc): "))

# Cálculo de la nota necesaria en la prueba escrita
Pe = (126 - 3 * Ep - 2 * Py - 2 * Pa - Pc) / 4

# Salida
print(f"La nota mínima que debe sacar en la prueba escrita (Pe) es: {Pe:.2f}")
