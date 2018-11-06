from abc import ABC, abstractmethod
import requests
import json
import sqlite3

class Pelicula():

    def __init__(self,id,titulo,genero,fecha_lanz,poster,rating,sinopsis,trailer=None,relacionados=None,link=None):

        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.fecha_lanz = fecha_lanz
        self.poster = poster
        self.rating = rating
        self.sinopsis = sinopsis
        self.trailer = trailer
        self.relacionados = relacionados
        self.link = link

class AbstractApi(ABC):
    @abstractmethod
    def get_pelicula(self, nombre):
        pass
        """Toma como parametro el nombre de la película y regresa un objeto de tipo película, la clase se que conecte al api implementa esta clase abstracta"""

class AbstractDb(ABC):
    @abstractmethod
    def crearTablaPeliculas(self):
        pass

    @abstractmethod
    def insertarPelicula(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula y regresa un objeto de tipo pelicula con los nuevos datos,
        la clase que se conecta a la base de datos implementa este metodo"""

    @abstractmethod
    def agregarTrailer(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula y regresa un objeto de tipo pelicula con los nuevos datos,
        la clase que se conecta a la base de datos implementa este metodo"""


    @abstractmethod
    def agregarRelacionados(self, pelicula):
        pass

    @abstractmethod
    def agregarLink(self, pelicula):
        pass


    @abstractmethod
    def consulta(self, pelicula):
        pass

    @abstractmethod
    def eliminarPelicula(self, pelicula):
        pass

class Sqlitedb(AbstractDb):
    def crearTablaPeliculas(self):
        conn = sqlite3.connect('peliculas.db')
        c = conn.cursor()
        if c.execute("""CREATE TABLE peliculas (
                    ID text,
                    TITULO text,
                    GENERO text,
                    FECHA_DE_LANZAMIENTO text,
                    POSTER text,
                    RATING text,
                    SINOPSIS text,
                    TRAILER text,
                    RELACIONADAS text,
                    LINK text
                    )"""):
                    print("Tabla creada con exito")
        else:
            print("Error al crear la tabla pelicula")
        conn.commit()
        conn.close()

    def insertarPelicula(self, pelicula):
        conn = sqlite3.connect('peliculas.db')
        c = conn.cursor()
        if c.execute("""INSERT INTO peliculas VALUES (
        :ID, :TITULO, :GENERO, :FECHA_DE_LANZAMIENTO, :POSTER, :RATING, :SINOPSIS, :TRAILER, :RELACIONADAS, :LINK)""",
        {'ID': pelicula.id, 'TITULO': pelicula.titulo, 'GENERO': pelicula.genero, 'FECHA_DE_LANZAMIENTO': pelicula.fecha_lanz, 'POSTER': pelicula.poster,
        'RATING': pelicula.rating, 'SINOPSIS': pelicula.sinopsis, 'TRAILER': pelicula.trailer, 'RELACIONADAS': pelicula.relacionados, 'LINK': pelicula.trailer}):
            print("Pelicula insertada con exito")
        else:
            print("Error al insertar la pelicula")
        conn.commit()
        conn.close()

    def agregarTrailer(self, pelicula):
        conn = sqlite3.connect("peliculas.db")
        #seleccionar el cursor para realizar la consulta
        c = conn.cursor()
        #sql = ("""UPDATE peliculas
        #SET trailer= "https://youtu.be/JcpWXaA2qeg"
        #WHERE id= :ID)""", {'ID': pelicula.id})

        c.execute("""UPDATE peliculas SET trailer= "https://youtu.be/JcpWXaA2qeg" WHERE id= :ID""", {'ID': pelicula.id})

        #terminamos la consulta
        #guardamos los cambios en la base de datos
        conn.commit()

        c.execute("SELECT * FROM PELICULAS")
        print(c.fetchall())
        conn.commit()

        #cerramos la conexion a la base de datos
        conn.close()

    def agregarRelacionados(self, pelicula):
        conn = sqlite3.connect("peliculas.db")
        #seleccionar el cursor para realizar la consulta
        c = conn.cursor()
        #sql = ("""UPDATE peliculas
        #SET trailer= "https://youtu.be/JcpWXaA2qeg"
        #WHERE id= :ID)""", {'ID': pelicula.id})

        c.execute("""UPDATE peliculas SET relacionadas= "IT 1, IT 2, IT 3" WHERE id= :ID""", {'ID': pelicula.id})

        #terminamos la consulta
        #guardamos los cambios en la base de datos
        conn.commit()

        c.execute("SELECT * FROM PELICULAS")
        print(c.fetchall())
        conn.commit()

        #cerramos la conexion a la base de datos
        conn.close()

    def agregarLink(self, pelicula):
        conn = sqlite3.connect("peliculas.db")
        #seleccionar el cursor para realizar la consulta
        c = conn.cursor()
        #sql = ("""UPDATE peliculas
        #SET trailer= "https://youtu.be/JcpWXaA2qeg"
        #WHERE id= :ID)""", {'ID': pelicula.id})

        c.execute("""UPDATE peliculas SET link= "https://www.cuevana2.com/pelicula/it/" WHERE id= :ID""", {'ID': pelicula.id})

        #terminamos la consulta
        #guardamos los cambios en la base de datos
        conn.commit()

        c.execute("SELECT * FROM PELICULAS")
        print(c.fetchall())
        conn.commit()

        #cerramos la conexion a la base de datos
        conn.close()

    def consulta(self, pelicula):
        conexion = sqlite3.connect("peliculas.db")
        #seleccionar el cursor para realizar la consulta
        consulta = conexion.cursor()


        consulta.execute(""" SELECT titulo FROM peliculas WHERE titulo= :titulo """, {'titulo': pelicula.titulo})

        #terminamos la consulta
        #guardamos los cambios en la base de datos
        conexion.commit()

        consulta.execute("SELECT * FROM PELICULAS")
        print(consulta.fetchall())
        conexion.commit()

        #cerramos la conexion a la base de datos
        conexion.close()

    def eliminarPelicula(self, pelicula):
        #conectar a la base de datos
        conexion = sqlite3.connect("peliculas.db")
        #seleccionar el cursor para realizar la consulta
        consulta = conexion.cursor()


        consulta.execute("""DELETE FROM peliculas WHERE titulo= :titulo """, {'titulo':pelicula.titulo})

        #terminamos la consulta
        #guardamos los cambios en la base de datos
        conexion.commit()

        consulta.execute("SELECT * FROM PELICULAS")
        print(consulta.fetchall())
        conexion.commit()

        #cerramos la conexion a la base de datos
        conexion.close()


#De aqui para abajo es lo que editaremos, es solo una idea
class OmdbApi(AbstractApi):
    def __init__(self,urlbase = "http://www.omdbapi.com/?", apikey = "2541db07", headers = {'Content-Type': 'application/json'}):
        self.urlbase = urlbase
        self.apikey = apikey
        self.headers = headers

    def get_pelicula(self, nombrepeli):
        api_url = '{0}&apikey={1}&t='.format(self.urlbase,self.apikey)+nombrepeli
        response = requests.get(api_url, headers=self.headers)
        if response.status_code == 200:
            contenidopelicula = json.loads(response.content.decode('utf-8'))
            if contenidopelicula is not None:
                print("Información: ")
                for k, v in contenidopelicula.items():
                    if k == 'imdbID':
                        print('ID:{}'.format(v))
                        id = v
                    if k == 'Title':
                        print('Título:{}'.format(v))
                        titulo = v
                    if k == 'Genre':
                        print('Género:{}'.format(v))
                        genero = v
                    if k == 'Released':
                        print('Fecha de lanzamiento:{}'.format(v))
                        fecha = v
                    if k == 'Poster':
                        print('Póster:{}'.format(v))
                        poster = v
                    if k == 'imdbRating':
                        print('Rating:{}'.format(v))
                        rating = v
                    if k == 'Plot':
                        print('Sinopsis:{}'.format(v))
                        sinopsis = v
                pelicula = Pelicula(id,titulo,genero,fecha,poster,rating,sinopsis)
                return pelicula
            else:
                print('[!] Request Failed')
        else:
            return None

if __name__ == '__main__':
    #Comentar o descomentar los metodos que se quieran probar, comentar crearTablaPeliculas una vez que ya se creo la tabla para
    api = OmdbApi()
    sqlite = Sqlitedb()
    sqlite.crearTablaPeliculas()
    pelicula = api.get_pelicula("It")
    sqlite.insertarPelicula(pelicula)
    sqlite.agregarTrailer(pelicula)
    sqlite.agregarRelacionados(pelicula)
    sqlite.agregarLink(pelicula)
    sqlite.consulta(pelicula)
    sqlite.eliminarPelicula(pelicula)
