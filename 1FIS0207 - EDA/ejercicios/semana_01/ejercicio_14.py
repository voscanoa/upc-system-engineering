"""Dada la hora actual (horas, minutos y segundos) determinar su equivalente en segundos."""

from datetime import datetime

hora_actual = datetime.now()

H = hora_actual.hour
m = hora_actual.minute
s = hora_actual.second

total_segundos = H * 3600 + m * 60 + s


print(
    f"La hora actual {H:02d}:{m:02d}:{s:02d} tiene un total de {total_segundos} segundos"
)
