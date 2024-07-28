# Using a flight data API called AviationStack

import requests
import config

# Function to get the flight information, with the parameter being the flight number
def get_API_info(flightNumber):
    apiKey = config.API_KEY
    params = {
        'access_key': apiKey,
        'flight_iata': flightNumber
    }
    # Decided to use and learn the Aviation Stack API as this API is a good choice for a project with small amount of requests
    apiURL = 'http://api.aviationstack.com/v1/flights'

    flights_results = requests.get(apiURL, params)

    if flights_results.ok:
        return flights_results.json()
    else:
        print("Unfortunately there was an error: ", flights_results.status_code)
        return None

# Function to format the time that is returned by the API
def format_time(time):
    if time:
        updatedTime = time.split("T")  # element at index 0 - time, element at index 1 - date
        return f"{updatedTime[1]}, {updatedTime[0]}"
    return "N/A"

# Function used to display the flight information, param is the entire flight Information list that the API gives with the matched flight number
def display_flight_info(flightInformation, flightInput):
    if flightInformation and 'data' in flightInformation:
        if flightInformation['data']:
            flight = flightInformation['data'][0]
            print(f"Airline: {flight['airline']['name']} ({flight['aircraft']['iata']})")
            print(f"Flight Number: {flight['flight']['iata']}")
            print(f"Flight Status: {flight['flight_status']}")
            print(f"Flight Date: {flight['flight_date']}")
            print(f"Departure Airport: {flight['departure']['airport']} ({flight['departure']['iata']})")
            print(f"Arrival Airport: {flight['arrival']['airport']} ({flight['arrival']['iata']})")
            print(f"Estimated Arrival Time: {format_time(flight['arrival']['estimated'])}")
            print(f"Actual Arrival Time: {format_time(flight['arrival']['actual'])}")
        else:
            print(f"Flight {flightInput} could not be found")
    else:
        print("Flight information is unavailable")


if __name__ == '__main__':
    flightInput = input("Enter the flight you'd like to track: ")

    flightInformation = get_API_info(flightInput)

    if flightInformation:
        display_flight_info(flightInformation, flightInput)
    else:
        print(f"Unable to retrieve and print flight {flightInput} information")
