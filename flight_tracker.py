# Using a flight data API called AviationStack

import requests
import config

# Function to get the flight information, with the parameter being the flight number
def get_flight_info(flightNumber):
    apiKey = config.API_KEY
    params = {
        'access_key' : apiKey
    }
    # Decided to use and learn the Aviation Stack API as this API is a good choice for a project with small amount of requests
    apiURL = 'http://api.aviationstack.com/v1/flights'

    flights_results = requests.get(apiURL, params)

    if flights_results.ok:
        return flights_results.json()
    else:
        print("Unfortunately there was an error: ", flights_results.status_code)
        return None

if __name__ == '__main__':
    flightInput = input("Enter the flight you'd like to track: ")

    flightInformation = get_flight_info(flightInput)

    if flightInformation:
        print(flightInformation)








