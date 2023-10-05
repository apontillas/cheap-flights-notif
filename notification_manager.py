from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ["AUTH_TOKEN"]
phone_num = os.environ["PHONE_NUMBER"]
twilio_num = os.environ["TWILIO_PHONE_NUMBER"]


class NotificationManager:
    def send_notif(self, data):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=data,
            from_= twilio_num,
            to= phone_num,
        )

        print(message.status)
        # print(data)
