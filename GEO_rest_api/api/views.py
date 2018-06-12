from django.shortcuts import render

# Create your views here.
import requests

def home(request):
    response = requests.get('http://freegeoip.net/json/')
    geodata = response.json()
    return render(request, 'home.html', {
        # 'ip': geodata['ip'],
        'country': geodata['country_name'],
        'state': geodata['region_name'],
        'city': geodata['city'],
        'code': geodata['zip_code'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
    })

def hi(request):
    return request("hiiiiii")

