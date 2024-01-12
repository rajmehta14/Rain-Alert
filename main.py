import requests
import os
from twilio.rest import Client
account_sid='ACebfdafc3d1f47013a7ff3d3f4e59b352'
auth_token="57eacdcf6876419dff3b7f3ff456ea15"
api_key=os .environ.get("owm_api_key")
LAT=23.0216238
LNG=72.5797068

parameters={
    "lat":LAT,
    "lon":LNG,
    "appid":api_key,
    "cnt":4,
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)

data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It will rain today",
                     from_="+18588425661",
                     to="+919428106168"
                 )
    print(message.status)



