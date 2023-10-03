from flight_search import FlightSearch

flight_search = FlightSearch()

class FlightData:
    def structure_data(self, flights_data):
            return {
            "city_from": flights_data['cityFrom'],
            "city_to": flights_data['cityTo'],
            "fly_from": flights_data['flyFrom'],
            "fly_to": flights_data['flyTo'],
            "cur_price": flights_data['price'],
            "from_date": flights_data['route'][0]['utc_departure'].split("T")[0],
            "to_date": flights_data['route'][1]['utc_departure'].split("T")[0],
            "seats": flights_data['availability']['seats'],
            "link": flights_data['deep_link']
            }
