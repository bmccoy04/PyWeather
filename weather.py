import requests
import json

cityState = raw_input("Enter the ciy, state you would like the weather for: ")

print(cityState)

requestUrl = 'http://apidev.accuweather.com/locations/v1/search?q=' + cityState + '&apikey=hoArfRosT1215'

req = requests.get(requestUrl)

data = json.loads(req.json())

print(data)
