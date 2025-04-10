import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv  # Create .env file first

load_dotenv()
api_key = os.getenv("WM_KEY")

# api_key = os.environ.get("WM_KEY")
print(f"WM_KEY: {api_key}")


print(str(api_key))
city = 'Lagos'
url = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 6.528490
MY_LNG = 3.355320
parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': api_key,
    'cnt': 7
}
response = requests.get(url=url, params=parameters)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)

account_sid = 'TWILLIO SID'
auth_token = 'TWILIO TOKEN'
client = Client(account_sid, auth_token)

will_rain = False
rain_time = []
for day in data['list']:
    time = day['dt_txt'].split(' ')[1]
    code = day['weather'][0]['id']
    weather = day['weather'][0]['description']
    if code < 700:
        will_rain = True
        rain_time.append(time)


if will_rain:
    rain_time_str = ' & '.join(rain_time)
    print(f'Bring an umbrella around {rain_time_str}')

    # message = client.messages.create(
    #   from_='TWILLIO NUMBER',
    #   body=f'Bring an umbrella around {rain_time_str}',
    #   to='RECEIVER'
    # )
    #
    # print(message.sid)
