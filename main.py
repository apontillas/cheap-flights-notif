from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from flight_data import FlightData


date_now = datetime.now()
DATE_FROM = date_now.strftime("%d/%m/%Y")
DATE_TO = (date_now + timedelta(days=6*30)).strftime("%d/%m/%Y") #"31/12/2023"
NIGHTS_MIN = 7
NIGHTS_MAX = 28
STOP_OVER = 1
# print(DATE_TO, DATE_FROM)

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

        data = search_flights.check_flights(fly_from_code=origin_code, fly_to_code=fly_to_code, date_from=DATE_FROM, date_to=DATE_TO, nights_max=NIGHTS_MAX, nights_min=NIGHTS_MIN, max_stopovers=STOP_OVER)
        try:
            data = data[0]
        except IndexError:
            continue
        else:
            flight = FlightData(data)
            if city['lowestPrice'] > flight.cur_price and flight.seats is not None:

                if flight.via_city.lower() in city['city'].lower():
                    print(flight.via_city, city['city'])
                    message.send_notif(
                        f"We found a cheap flight from {flight.city_from} ({flight.fly_from}) to {flight.city_to} ({flight.fly_to}) for ONLY ${flight.cur_price}! \nFrom {flight.from_date} to {flight.to_date}. Only {flight.seats} seat(s) left.")
                    print(fly_to_code, flight.link)
                else:
                    message.send_notif(
                        f"We found a cheap flight from {flight.city_from} ({flight.fly_from}) to {flight.city_to} ({flight.fly_to}) for ONLY ${flight.cur_price}! \nFrom {flight.from_date} to {flight.to_date}. Flight has {flight.stop_overs} stopover via {flight.via_city}. Only {flight.seats} seat(s) left.")
                    print(fly_to_code, flight.link)
get_lowest_fare()


