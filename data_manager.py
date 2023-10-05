import requests as req
import os


GET_ENDPOINT = "https://api.sheety.co/3c438d2e7b1a74f53805fda64cb0e402/flightDeals"
sheety_auth = os.environ['SHEETY_AUTH']

header = {
    'Authorization': sheety_auth,
}

class DataManager:
    def get_cities(self, call_sheety: bool = False) -> list:
        if call_sheety:
            res = req.get(url=f"{GET_ENDPOINT}/prices")
            city_data = res.json()['prices']
        else:
            city_data = [{"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
                         {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
                         {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
                         {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
                         {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
                         {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
                         {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
                         {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
                         {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
                         {"city": "Manila", "iataCode": "MNL", "lowestPrice": 600, "id": 11},
                         {"city": "Bali", "iataCode": "DPS", "lowestPrice": 200, "id": 12}]

        return city_data



    def update_iata(self, row, code):
        body = {
            "price": {
                "iataCode": code,
            }
        }

        res = req.put(url=f"{GET_ENDPOINT}/prices/{row}", json=body, headers=header)
        # print(res.text)

    def get_recipients(self, call_sheety: bool = False) -> list:
        if call_sheety:
            res = req.get(url=f"{GET_ENDPOINT}/users")
            users = res.json()['users']
        else:
            users = [{"firstName": 'Angely', "lastName": 'Pontillas', "email": 'a@gmail.com'}]
        return users



