import requests
import json

class ForwardGeocoder():
    """
    """
    def __init__(self, apiKey: str):
        self.apiKey = apiKey
        self.base_url = "https://geocode.search.hereapi.com/v1/geocode"

    def parser(self, data):
        coordinates = []
        json_data = data.json()
        coordinates.append(json_data["items"][0]["position"]["lat"])
        coordinates.append(json_data["items"][0]["position"]["lng"])
        return print(coordinates)


    def geocode(self, adress_line: str):
        params = {
            "q": adress_line,
            "apiKey": self.apiKey  
        }
        respond = requests.get(self.base_url, params=params)
        self.parser(respond)
        # return print(respond.text)

