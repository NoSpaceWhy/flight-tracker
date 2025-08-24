import requests

def flightRQ():
    # OpenSky REST API (anonymous has limited range)
    url = "https://opensky-network.org/api/states/all"

    response = requests.get(url)
    data = response.json()

    # Print first 5 flights
    for flight in data['states'][:5]:
        call_sign = flight[1]
        country = flight[2]
        lat = flight[6]
        lon = flight[5]
        flightsData = f"Flight {call_sign} from {country} at {lat}, {lon}"
    return flightsData