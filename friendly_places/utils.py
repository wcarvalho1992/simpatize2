from simpatize.settings import GOOGLE_PLACES_API_KEY
from simpatize.settings import LATITUDE
from simpatize.settings import LONGITUDE
from friendly_places.models import Place
import requests

class GooglePlacesQueries:
	def prepare(self, request):
		self.url = Url().create(request).get()
		return self

	def do_request(self):
		self.results = requests.get(self.url).json()
		return self

	def get_results(self):
		return [Place(name = item['name']) for item in self.results['results']]

class Url:
	def create(self, request):
		parameters = dict(request.GET)
		parameters['location'] = "{},{}".format(LATITUDE, LONGITUDE)
		parameters['radius'] = "20000"
		self.url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={}".format(GOOGLE_PLACES_API_KEY)
		[self.add_query_string(item, self.remove_index_chars(str(parameters[item]))) for item in parameters]
		return self

	def add_query_string(self, key, value):
		self.url = self.url + "&{}={}".format(key, value)

	def remove_index_chars(self, str):
		return str.replace("['", "").replace("']", "") if "['" in str else str

	def get(self):
		return self.url
