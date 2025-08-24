import requests
import random

def flightRQ():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    data = response.json()

    # Pick a random flight so it changes every call
    flight = random.choice(data['states'])
    call_sign = flight[1]
    country = flight[2]
    lat = flight[6]
    lon = flight[5]
    return f"Flight {call_sign} from {country} at {lat}, {lon}"
