from flight_search import FlightSearch

flight_search = FlightSearch()

class FlightData:
        def __init__(self, flights_data):
            self.city_from = flights_data['cityFrom']
            self.city_to = flights_data['cityTo']
            self.fly_from = flights_data['flyFrom']
            self.fly_to = flights_data['flyTo']
            self.cur_price = flights_data['price']
            self.from_date = flights_data['route'][0]['utc_departure'].split("T")[0]
            self.to_date = flights_data['route'][1]['utc_departure'].split("T")[0]
            self.seats = flights_data['availability']['seats']
            self.link = flights_data['deep_link']
            self.via_city = flights_data['route'][0]['cityTo']
            self.stop_overs = (len(flights_data['route']) / 2) - 1



