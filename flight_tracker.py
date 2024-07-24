# Using a flight data API called AviationStack

import requests
import config

# Function to get the flight information, with the parameter being the flight number
def get_flight_info(flight_number):
    apiKey = config.API_KEY
    params = {
        'access_key' : config.API_KEY
    }
    # Decided to use and learn the Aviation Stack API as this API is a good choice for a project with small amount of requests
    apiURL = 'http://api.aviationstack.com/v1/flights'

    flights_results = requests.get(apiURL, params)
    aviationstack_info = flights_results.json()





