import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "0449ca79eeda3540284c8b4fcbb0ea0a"
account_sid = "AC26c3ec14816eb3e6f3fbdfdb69cfec5e"
auth_token = "8f507b0b86c390f2411983e54b2a041e"


weather_params = {
    # "lat": 31.8186,
    # "lon": 75.2028,
    "lat": 49.710900,
    "lon": 4.914250,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}


response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+19036646101",
        to="+919646176517",
    )
    print(message.status)


