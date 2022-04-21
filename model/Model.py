'''
Python model class defined here.
'''

import requests

API_KEY = '9c755385b6mshac6000144a4ed40p1e251ajsn016da9ab136c'
API_URL = 'https://weather-by-api-ninjas.p.rapidapi.com/v1/weather'

# Required headers for RapidAPI requests:
headers = {'x-rapidapi-host': 'weather-by-api-ninjas.p.rapidapi.com',
           'x-rapidapi-key': API_KEY}


class Model:
    '''
    Implementation of the Model controller class.
    '''
    data = {}
    
    def __init__(self):
        # The empty dictionary object for storing forecast data.
    	self.data = {}
    	
    def get_data(self):
    	"""
    	Getter function for the data dictionary.
    	"""
    	return self.data
    
    def search_city(self, city):
        """
        Submits search request for the forecast of specified city
        :return: Dictionary of forecast elements for specified city
        """

        querystring = {'city': city}
        response = requests.request('GET', API_URL, headers=headers,
                                    params=querystring)
        self.data = response.json()
        return self.data

    def search_zip(self, zip):
        """
    ....Submits search request for the forecast of specified zip code
    ....:return: Dictionary of forecast elements for specified zip code
    ...."""

        querystring = {'zip': zip}
        response = requests.request('GET', API_URL, headers=headers,
                                    params=querystring)
        self.data = response.json()
        return self.data

