from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from flight_data import FlightData
import os


date_now = datetime.now()
DATE_FROM = date_now.strftime("%d/%m/%Y")
DATE_TO = (date_now + timedelta(days=6*30)).strftime("%d/%m/%Y")
NIGHTS_MIN = 7
NIGHTS_MAX = 28
STOP_OVER = 1
sender = os.environ["EMAIL"]
password = os.environ["EMAIL_PASSWORD"]


search_flights = FlightSearch()
data = DataManager()
message = NotificationManager()
cities = data.get_cities()
codes = search_flights.get_codes()
recipients = data.get_recipients()

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
            msg = f"We found a cheap flight from {flight.city_from} ({flight.fly_from}) to {flight.city_to} ({flight.fly_to}) for ONLY ${flight.cur_price}! \nFrom {flight.from_date} to {flight.to_date}. Only {flight.seats} seat(s) left."

            if city['lowestPrice'] > flight.cur_price and flight.seats is not None:

                if flight.via_city.lower() in city['city'].lower():
                    print(flight.via_city, city['city'])
                    message.send_sms(msg)
                    print(fly_to_code, flight.link)

                    [message.send_email(sender=sender, password=password, recipient=recipient['email'],
                                        msg=f"Subject: We found cheap flights for you {recipient['firstName']}! \n\n{msg}. Here is the link: {flight.link}") for recipient in recipients]
                else:
                    message.send_sms(f"{msg}. Flight has {flight.stop_overs} stopover via {flight.via_city}.")
                    [message.send_email(sender=sender, password=password, recipient=recipient['email'],
                                        msg=f"Subject: We found cheap flights for you {recipient['firstName']}! \n\n{msg}. Flight has {flight.stop_overs} stopover via {flight.via_city}. Here is the link: {flight.link}")
                     for recipient in recipients]


get_lowest_fare()


