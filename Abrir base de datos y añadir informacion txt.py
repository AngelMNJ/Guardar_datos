import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("datos.db")
cursor = conn.cursor()
cursor.execute('SELECT * FROM Usuarios')
# Recupera todas las filas
rows = cursor.fetchall()
# Una fila solo
'''
row = cursor.fetchone()
'''
archivo = open("datos.txt", "a")
archivo.write('\n')
for row in rows:
    archivo.write(str(row) + '\n')
archivo.close()

for row in rows:
    print(row)

conn.close()
