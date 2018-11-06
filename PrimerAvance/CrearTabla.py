import sqlite3
#conectar a la base de datos
conexion = sqlite3.connect("peliculas.db")
#seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()
sql = ("""CREATE TABLE PELICULAS(
ID text,
TITULO text,
GENERO text,
FECHA_DE_LANZAMIENTO DATE NOT NULL,
POSTER text,
RATING text,
SINOPSIS text,
TRAILER text,
RELACIONADAS text,
LINK text)""")
consulta.execute(sql)



#terminamos la consulta
consulta.close()
#guardamos los cambios en la base de datos
conexion.commit()
#cerramos la conexion a la base de datos
conexion.close()
