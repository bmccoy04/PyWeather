import requests
import json

cityState = input("Enter the ciy, state you would like the weather for: ")

print(cityState)

requestUrl = 'http://apidev.accuweather.com/locations/v1/search?q=' + cityState + '&apikey=hoArfRosT1215'

req = requests.get(requestUrl)

data = req.json()

for d in data:
    print(d)