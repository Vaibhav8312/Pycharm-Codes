from twilio.rest import Client
import smtplib

TWILIO_SID = "AC26c3ec14816eb3e6f3fbdfdb69cfec5e"
TWILIO_AUTH_TOKEN = "8f507b0b86c390f2411983e54b2a041e"
TWILIO_VIRTUAL_NUMBER = "+19036646101"
TWILIO_VERIFIED_NUMBER = "+919646176517"

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "chitkarauniversity38@gmail.com"
MY_PASSWORD = "abcd1234()"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )