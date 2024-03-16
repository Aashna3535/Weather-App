from django.shortcuts import render
import requests

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4ec493f5ec0a3e5207c9aed25474ea62'
    city = 'London'  # Default city
    response = requests.get(url.format(city)).json()
    
    weather_data = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],

    }
    return render(request, 'home.html', {'weather_data': weather_data})
