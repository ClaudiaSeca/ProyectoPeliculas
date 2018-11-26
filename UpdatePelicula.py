import sqlite3
#método agregar pelicula

#conectar a la base de datos
conexion = sqlite3.connect("peliculas.db")
#seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()
sql = ("""UPDATE peliculas
SET id= "ee1396485", titulo= "Toy Story 3", genero= "Comedia",
fecha_de_lanzamiento= "18 JUN 2010", poster= "http://images.telemetro.com/blogs/geekture/Datos-Toy-Story-conocias_MEDIMA20151127_0201_3.jpg",
ratings= "8.3", sinopsis= "Andy va a la universidad", trailer= "https://youtu.be/JcpWXaA2qeg",
relacionadas= "Toy Story, Toy Story 2", link= "http://gnula.nu/animacion-infantil/ver-toy-story-3-2010-online/" WHERE id= 'tt1396484' """)

consulta.execute(sql)

#terminamos la consulta
#guardamos los cambios en la base de datos
conexion.commit()

consulta.execute("SELECT * FROM PELICULAS")
print(consulta.fetchall())
conexion.commit()

#cerramos la conexion a la base de datos
conexion.close()
