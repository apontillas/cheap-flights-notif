import requests as req
from data_manager import DataManager
import os

KIWI_API = "https://api.tequila.kiwi.com"
kiwi_api_key = os.environ["KIWI_API_KEY"]

flight_data = DataManager()
cities = flight_data.get_cities()

class FlightSearch:
    def get_codes(self):
        codes = []
        header = {
            "apikey": kiwi_api_key,
        }

        for city in cities:
            query = {
               "term": city['city'],
                "location_types": 'city'
            }
            res = req.get(url=f"{KIWI_API}/locations/query", params=query, headers=header)
            code_data = res.json()['locations']
            codes.append(code_data[0]['code'])
            # print(code_data[0])
        return codes


    def check_flights(self, fly_from_code, fly_to_code, date_from, date_to, nights_min, nights_max, max_stopovers=0):

        header = {
            "apikey": kiwi_api_key,
        }
        query = {
            "fly_from": fly_from_code,
            "fly_to": fly_to_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": nights_min,
            "nights_in_dst_to": nights_max,
            "max_stopovers": max_stopovers,
            "curr": "USD",
            "flight_type": "round",
        }
        search_endpoint = f"{KIWI_API}/v2/search"
        res = req.get(url=search_endpoint, params=query, headers=header)
        flights_data = res.json()['data']
        # print(flights_data)

        return flights_data
