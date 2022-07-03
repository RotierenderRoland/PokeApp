import requests

class api_connector:
    def connect(url):
        response=requests.get(url)
        return response.json()

    def status(url):
        if requests.get(url).status_code == 200:
            return requests.get(url).json()["id"]
        else:
            return False

class Pokemon:
    def __init__(self,response):
        self.id=response["id"]
        self.name=response["species"]["name"]
        self.is_default=response["is_default"]
        self.abilities=[response["abilities"][i]["ability"]["name"]for i in range(len(response["abilities"]))]
        self.height=response["height"]
        self.base_experience=response["base_experience"]
        self.weight=response["weight"]
        self.types=[response["types"][i]["type"]["name"]for i in range(len(response["types"]))]
        
