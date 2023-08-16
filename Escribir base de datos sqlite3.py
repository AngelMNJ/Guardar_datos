import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect("datos.db")

# Crear una tabla
conexion.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)")

# Insertar datos en la tabla
conexion.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 25))
conexion.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("María", 30))

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
