from abc import ABC, abstractmethod
import requests
import json

class Pelicula():

    def __init__(self,id,titulo,genero,fecha_lanz,poster,ratings,sinopsis,trailer=None,relacionados=None,link=None):

        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.fecha_lanz = fechalanz
        self.poster = poster
        self.ratings = ratings
        self. sinopsis = sinopsis

class AbstractApi(ABC):
    @abstractmethod
    def get_pelicula(self, nombre):
        pass
        """Toma como parametro el nombre de la película y regresa un objeto de tipo película, la clase se que conecte al api implementa esta clase abstracta"""

class AbstractDb(ABC)
    @abstractmethod
    def crearPelicula(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula y regresa un objeto de tipo pelicula con los nuevos datos,
        la clase que se conecta a la base de datos implementa este metodo"""

# De aqui para abajo es lo que editaremos, es solo una idea
class OmdbApi(AbstractApi):
    def __init__(self,urlbase = "http://www.omdbapi.com/?",apikey = 2541db07, headers = {'Content-Type': 'application/json'}):
        self.urlbase = urlbase
        self.apikey = apikey
        self.headers = headers

    def get_pelicula(self, nombre):

    api_url = '{0}&apikey={}&t='.format(api_url_base)+nombre
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

    def connect():
        res = requests.get("www.omdbapi.com/?t=the+purge&apikey={}".format(self.apikey))
        self.token = res.token
