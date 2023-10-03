from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from flight_data import FlightData


date_now = datetime.now()
DATE_FROM = date_now.strftime("%d/%m/%Y")
DATE_TO = (date_now + timedelta(days=6*30)).strftime("%d/%m/%Y") #"31/12/2023"
STOPOVER = 0
NIGHTS_MIN = 7
NIGHTS_MAX = 28

search_flights = FlightSearch()
flight_data = FlightData()
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

        data = search_flights.check_flights(fly_from_code=origin_code, fly_to_code=fly_to_code, date_from=DATE_FROM, date_to=DATE_TO, nights_max=NIGHTS_MAX, nights_min=NIGHTS_MIN, max_stopovers=STOPOVER)
        if len(data) > 0:
            data = data[0]
            flight = flight_data.structure_data(data)

            if city['lowestPrice'] > flight['cur_price'] and flight['seats'] is not None:
                message.send_notif(
                    f"We found a cheap flight from {flight['city_from']} ({flight['fly_from']}) to {flight['city_to']} ({flight['fly_to']}) for ONLY ${flight['cur_price']}! \nFrom {flight['from_date']} to {flight['to_date']}. Only {flight['seats']} seat(s) left.")
                print(fly_to_code, flight['link'])
        else:
            continue



get_lowest_fare()
