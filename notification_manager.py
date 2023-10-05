from twilio.rest import Client
import os
import smtplib


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ["AUTH_TOKEN"]
phone_num = os.environ["PHONE_NUMBER"]
twilio_num = os.environ["TWILIO_PHONE_NUMBER"]


class NotificationManager:
    def send_sms(self, data):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=data,
            from_= twilio_num,
            to= phone_num,
        )

        print(message.status)
        # print(data)

    def send_email(self, sender, password, recipient, msg):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender, password=password)
            connection.sendmail(from_addr=sender, to_addrs=recipient, msg=msg)



