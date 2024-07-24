# Using a flight data API called AviationStack

import requests
import config

apiKey = config.API_KEY
params = {
    'aviation_stack_access_key' : apiKey
}
# Decided to use and learn the Aviation Stack API as this API is a good choice for a project with small amount of requests
apiURL = 'http://api.aviationstack.com/v1/flights'
