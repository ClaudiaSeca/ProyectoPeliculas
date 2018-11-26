import sqlite3
#método agregar pelicula

#conectar a la base de datos
conexion = sqlite3.connect("peliculas.db")
#seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()
sql = ("""INSERT INTO PELICULAS VALUES ("tt1396484", "IT",
"TERROR", "08 SEP 2017", "https://i.blogs.es/26e0e3/pennywise1/450_1000.jpg",
"7.4", "Niños desaperecen misteriosamente", "https://youtu.be/FnCdOQsX5kc",
"Decidelo Tú, Las Cuatro Despues de la media noche, INSDIOUS", "https://gnula.gratis/it-1/")""")

consulta.execute(sql)

#terminamos la consulta
#guardamos los cambios en la base de datos
conexion.commit()

consulta.execute("SELECT * FROM PELICULAS")
print(consulta.fetchall())
conexion.commit()

#cerramos la conexion a la base de datos
conexion.close()
