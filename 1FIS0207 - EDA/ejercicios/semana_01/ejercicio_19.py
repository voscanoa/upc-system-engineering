"""Estimar el número de páginas de un texto que puede almacenarse en la memoria de un computador, considerando un promedio de 300 palabras por página y 10 caracteres por palabra. Asumir que un carácter ocupa un byte. El tamaño de la memoria del computador debe ingresarse expresado en Kbytes."""

memoria_KB = float(input("Ingresar la cantidad de memoria: "))
memoria_bytes = memoria_KB * 1024
bytes_por_pagina = 300 * 10
paginas = memoria_bytes / bytes_por_pagina
print(f"La cantidad de paginas es {paginas:.2f}")
