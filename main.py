import requests
import os
from twilio.rest import Client


OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "fake_key"
account_sid = "another_fake_key"
auth_token = "another_one"

#loaction of new york in terms of lattitude and longitude
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
