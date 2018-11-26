import sqlite3
#método agregar pelicula

#conectar a la base de datos
conexion = sqlite3.connect("peliculas.db")
#seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

sql = ("""SELECT titulo FROM peliculas WHERE titulo= 'Toy Story 3' """)

consulta.execute(sql)

#terminamos la consulta
#guardamos los cambios en la base de datos
conexion.commit()

consulta.execute("SELECT * FROM PELICULAS")
print(consulta.fetchall())
conexion.commit()

#cerramos la conexion a la base de datos
conexion.close()
