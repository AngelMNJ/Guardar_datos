import csv

# Datos a guardar
datos = [
    ["Nombre", "Edad"],
    ["Juan", 25],
    ["María", 30]
]

# Abrir el archivo CSV en modo escritura
with open("datos.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo, delimiter=';')

    # Escribir los datos en el archivo
    for fila in datos:
        escritor.writerow(fila)
