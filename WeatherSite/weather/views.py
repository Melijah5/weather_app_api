from django.shortcuts import render
import pandas as pd
import requests
# Create your views here.
def index(request):
    df = pd.read_csv('worldcities.csv')
    if 'city' in request.GET:
        city = request.GET['city']
        if df[df['city_ascii'] == city]['city_ascii'].any():
            lat = df[df['city_ascii'] == city]['lat'] 
            log = df[df['city_ascii'] == city]['lng']
            url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"

        querystring = {"unit_system": "si","fields": ["precipitation", "precipitation_type", "temp", "cloud_cover", "wind_speed","weather_code"],"lat": lat,"lon":log}

        headers = {
            'x-rapidapi-key': "6e9c9a10b3mshed5fde96db16b37p149609jsn35fb89b0ec76",
            'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        context = {'city_name': city, 'temp': response['temp']['value'], 'weather_code':response['weather_code']['value'],'wind_speed':response['wind_speed']['value'],'precipitation_type': response['precipitation_type']['value'] }
            
        print(response)
        return render(request, 'weather/index.html', context)