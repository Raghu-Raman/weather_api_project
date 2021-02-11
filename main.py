import requests
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure


OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "fa8da426ef3c25226b795cd9263cb522"
account_sid = "AC3262777e01cb1e81898a2c5433e0dc4f"
auth_token = "14c83ffdebf4d2638f2c5fb290dbb7a8"

weather_params = {
    "lat": 40.7128,
    "lon":	74.0060,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OMW_Endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()
need_umbrella = False
for i in range(0, 12):
    if int(weather_data["hourly"][i]["weather"][0]["id"]) < 700:
         need_umbrella = True
# print(weather_data)
# if need_umbrella:
#     print("umbrella")
# else:
#     print("No umbrellA")

client = Client(account_sid, auth_token)

if not need_umbrella:
    message = client.messages \
        .create(
        body=f"It will not rain for the next 12 hours. Latitude={weather_params['lat']} ,Longitude={weather_params['lon']}"
             "XOXO-digudii",
        from_="+16514096517",
        to="+918870668292"
    )
    print(message.status)
else:
    message = client.messages \
        .create(
        body=f"It will not rain for the next 12 hours. Latitude={weather_params['lat']} ,Longitude={weather_params['lon']}"
             "XOXO-digudii",
        from_="+16514096517",
        to="+918870668292"
    )
    print(message.status)