import unittest
import Implementacion

#Testear el insert
class TestInsertar(unittest.TestCase):
	def setUp(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()

		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")

		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def tearDown(self):
		#Se elimina toda la información de la bd para no generar problemas con otros test
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()


	def test_Insert(self):
		PeliculaExiste = Implementacion.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		Prueba = Implementacion.Sqlitedb.insertarPelicula(self, PeliculaExiste)
		self.assertEqual(Prueba, [('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')])


		Prueba = Implementacion.Sqlitedb.insertarPelicula(self, 'navidad en la FAC')
		self.assertEqual(Prueba, "No se pudo agregar la pelicula a la tabla, probablemente no está en la api")


class TestDelete(unittest.TestCase):

#Se crea la tabla peliculas antes de iniciar el test para que no haya problemas en los querys y se insertan peliculas para eliminar
	def setUp(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()

		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4',
		'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd',
		'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")

		conn.commit()
		conn.close()

#Se elimina toda la información de la bd para no generar problemas con otros test
	def tearDown(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()


	def test_eliminarPelicula(self):

		#Caso de prueba donde se elimna una película que si existe y que se recibio un objeto pelicula como parametro
		#Se espera recibir una lista vacía
		pelicula = Implementacion.Pelicula('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4',
		'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd',
		'Spider Man 2, Spider Man 3', 'www.cuevana.com')
		resultado = Implementacion.Sqlitedb.eliminarPelicula(self, pelicula)
		self.assertEqual(resultado, [])

		#Caso de prueba donde se elimna una película que no existe y que se recibio un objeto pelicula como parametro
		#Se espera recibir un string de error con la eliminacion
		pelicula = Implementacion.Pelicula('111111111', 'It', 'Drama, Horror, Thriller', '08 Sep 2017',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether',
		'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Implementacion.Sqlitedb.eliminarPelicula(self, pelicula)
		self.assertEqual(resultado, "No se puede eliminar la película porque no está en la base de datos")

		#Caso de prueba donde se elimna una película que no existe y que se recibio un Nulo como parametro
		#Se espera recibir un string de error con la eliminacion
		resultado2 = Implementacion.Sqlitedb.eliminarPelicula(self, None)
		self.assertEqual(resultado, "No se puede eliminar la película porque no está en la base de datos")

class TestUpdate(unittest.TestCase):

#Se crea la tabla peliculas antes de iniciar el test para que no haya problemas en los querys
#Se insertan peliculas en la BD que serán actualizadas en los casos de prueba
	def setUp(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()

		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9',
		'A student obtain powers from a spider', Null, Null, Null)""")

		conn.commit()
		conn.close()

#Se elimina toda la información de la bd para no generar problemas con otros test
	def tearDown(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_agregarLink(self):
		#Caso de prueba donde se intenta actualizar una pelicula que no existe en la BD
		#Se espera un string notificando error
		pelicula = Implementacion.Pelicula('111111111', 'It', 'Drama, Horror, Thriller', '08 Sep 2017',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4',
		'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Implementacion.Sqlitedb.agregarLink(self, pelicula, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado, "No se puede actualizar el link de la película porque no está en la base de datos")

		#Caso de prueba donde se intenta actualizar una pelicula pasando un parametro None
		#Se espera un string notificando error
		resultado2 = Implementacion.Sqlitedb.agregarLink(self, None, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado2, "No se puede actualizar el link de la película porque no está en la base de datos")

		#Caso de prueba donde se actualiza el link de una pelicula existente en la BD
		#Se espera recibir una lista de la pelicula actualizada con el nuevo link
		pelicula2 = Implementacion.Pelicula('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')
		resultado3 = Implementacion.Sqlitedb.agregarLink(self, pelicula2, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado3, [('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'Youtube.com/watch=gdhbsjkvdh3')])

		#Caso de prueba donde se actualiza el link de una pelicula existente pero que no tiene los datos completos en la BD
		#Se espera recibir una lista de la pelicula actualizada con el nuevo link en ligar de un None
		pelicula3 = Implementacion.Pelicula('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)
		resultado4 = Implementacion.Sqlitedb.agregarLink(self, pelicula3, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado4, [('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider',
		None, None, 'Youtube.com/watch=gdhbsjkvdh3')])

class TestSelect(unittest.TestCase):

#Se crea la tabla peliculas antes de iniciar el test para que no haya problemas en los querys
#Se insertan peliculas en la BD que serán buscadas en los casos de prueba
	def setUp(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider',
		Null, Null, Null)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg',
		'7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3',
		'www.cuevana.com')""")

		conn.commit()
		conn.close()

#Se elimina toda la información de la bd para no generar problemas con otros test
	def tearDown(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_consultarPelicula(self):
		#Caso de prueba donde se busca una pelicula existente en la BD
		#Se espera una lista
		pelicula = Implementacion.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether',
		'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Implementacion.Sqlitedb.consultarPelicula(self, pelicula)
		self.assertEqual(resultado, [('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether',
		'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')])

		#Caso de prueba donde se busca una pelicula que no existe en la BD
		#Se espera un string notificando error
		resultado2 = Implementacion.Sqlitedb.consultarPelicula(self, None)
		self.assertEqual(resultado2, "La película que buscas no está en la base de datos")

		#Caso de prueba donde se busca una pelicula no existente en la BD
		#Se espera un string notificando error
		pelicula2 = Implementacion.Pelicula('fbhesl%$#$', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')
		resultado3 = Implementacion.Sqlitedb.consultarPelicula(self, pelicula2)
		self.assertEqual(resultado3, "La película que buscas no está en la base de datos")

		#Caso de prueba donde se busca una pelicula existente en la BD pero tiene datos incompletos
		#Se espera una lista con los datos de la pelicula
		pelicula3 = Implementacion.Pelicula('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)
		resultado4 = Implementacion.Sqlitedb.consultarPelicula(self, pelicula3)
		self.assertEqual(resultado4, [('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)])

class TestGetSqlite(unittest.TestCase):

#Se crea la tabla peliculas antes de iniciar el test para que no haya problemas en los querys
#Se insertan peliculas en la BD que serán buscadas en los casos de prueba
	def setUp(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()

		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider',
		Null, Null, Null)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg',
		'7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3',
		'www.cuevana.com')""")

		conn.commit()
		conn.close()

#Se elimina toda la información de la bd para no generar problemas con otros test
	def tearDown(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_get_pelicula(self):

		#Caso de prueba donde se obtiene una pelicula con un titulo de la base de datos con un titulo de una pelcula existente
		#Se comparan los id's
		res = Implementacion.Sqlitedb.get_pelicula(self, "It")
		pelicula = Implementacion.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether',
		'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		self.assertEqual(res.id, pelicula.id)

		#Caso de prueba donde se intenta obtener una película con un titulo no existente en la BD
		#Se espera recibir un None
		res2 = Implementacion.Sqlitedb.get_pelicula(self, "bhdlfnjla")
		self.assertEqual(res2, None)

		#Caso de prueba donde se obtiene una pelicula de la base de datos con un titulo de una pelcula existente pero está con datos incompletos
		#Se comparan los id's
		res3 = Implementacion.Sqlitedb.get_pelicula(self, 'Spider Man 2')
		pelicula2 = Implementacion.Pelicula('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)
		self.assertEqual(res3.id, pelicula2.id)

class TestGetOMDBApi(unittest.TestCase):

#Se crea la tabla peliculas antes de iniciar el test para que no haya problemas en los querys
#Se insertan peliculas en la BD que serán buscadas en los casos de prueba
	def setUp(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()

		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider',
		'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005',
		'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', Null, Null, Null)""")

		c.execute("""INSERT INTO peliculas VALUES (
		'tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg',
		'7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')""")

		conn.commit()
		conn.close()

#Se elimina toda la información de la bd para no generar problemas con otros test
	def tearDown(self):
		conn = Implementacion.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_get_pelicula(self):
		api = Implementacion.OmdbApi()
		res = Implementacion.OmdbApi.get_pelicula(api, "It")

		#Caso de prueba donde se obtiene una pelicula de la api con un titulo de una pelcula existente
		#Se comparan los id's
		pelicula = Implementacion.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg',
		'7.4', 'In the summer of 1989, agroup of kids band toghether to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.',
		'http://youtube.com/whatch=ruefonhfkjdnknd')
		self.assertEqual(res.id, pelicula.id)

		#Caso de prueba donde se obtiene una pelicula de laapi con un titulo de una pelcula no existente
		#Se espera un string notificando error
		res2 = Implementacion.OmdbApi.get_pelicula(api, "562re7gdwqud")
		self.assertEqual(res2, "No se encontró la pelicula en la Api")

		#Caso de prueba donde se obtiene una pelicula de la api con un titulo mas complejo en caracteres de una pelcula existente
		#Se comparan los id's
		res3 = Implementacion.OmdbApi.get_pelicula(api, 'Toy Story 3')
		pelicula2 = Implementacion.Pelicula("tt0435761", 'Toy Story 3', 'Animation, Adventure, Comedy, Family, Fantasy',
		'18 Jun 2010', "https://m.media-amazon.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg", '8.3',
		"The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
		None, None, None)
		self.assertEqual(res3.id, pelicula2.id)

"""class TestDelete(unittest.TestCase):
	def test_Delete(self):

		Prueba2 = eliminarPelicula.(REC2)
		self.assertEqual(Prueba2, REC2)

#Testear el update
class TestUpdate(unittest.TestCase):
	def test_Update(self):

		Prueba3 = eliminarPelicula.(REC2)
		self.assertEqual(Prueba3, REC2)"""



if __name__ == '__main__':


	unittest.main()
