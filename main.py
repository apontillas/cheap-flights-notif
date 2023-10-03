from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

date_now = datetime.now()
DATE_FROM = date_now.strftime("%d/%m/%Y")
DATE_TO = (date_now + timedelta(days=6*30)).strftime("%d/%m/%Y") #"31/12/2023"
STOPOVER = 0
NIGHTS_MIN = 7
NIGHTS_MAX = 28

search_flights = FlightSearch()
data = DataManager()
message = NotificationManager()
cities = data.get_cities()
codes = search_flights.get_codes()

for i in range(len(codes)):
    # Populate in Google Sheets
    data.update_iata(i+2, codes[i])

def get_lowest_fare():
    origin_code = "ATL"
    for city in cities:
        fly_to_code = city['iataCode']
        # print(fly_to_code)

        flights_data = search_flights.check_flights(fly_from_code=origin_code, fly_to_code=fly_to_code, date_from=DATE_FROM, date_to=DATE_TO, nights_max=NIGHTS_MAX, nights_min=NIGHTS_MIN, max_stopovers=STOPOVER)
        if len(flights_data) > 0:
            flights_data = flights_data[0]

            city_from = flights_data['cityFrom']
            city_to = flights_data['cityTo']
            fly_from = flights_data['flyFrom']
            fly_to = flights_data['flyTo']
            cur_price = flights_data['price']
            from_date = flights_data['route'][0]['utc_departure'].split("T")[0]
            to_date = flights_data['route'][1]['utc_departure'].split("T")[0]
            seats = flights_data['availability']['seats']
            link = flights_data['deep_link']

            if city['lowestPrice'] > cur_price and seats is not None:
                message.send_notif(
                    f"We found a cheap flight from {city_from} ({fly_from}) to {city_to} ({fly_to}) for ONLY ${cur_price}! \nFrom {from_date} to {to_date}. Only {seats} seat(s) left.")
                print(fly_to_code, link)
        else:
            continue



get_lowest_fare()
