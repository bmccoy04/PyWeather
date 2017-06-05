import requests
import sys
import json

#print(sys.argv)

location_url = 'http://freegeoip.net/json'

r = requests.get(location_url)
location = json.loads(r.text)

cityState = location['city'] + ', ' + location['region_code']   ##input("Enter the ciy, state you would like the weather for: ")

requestUrl = 'http://apidev.accuweather.com/locations/v1/search?q=' + cityState + '&apikey=hoArfRosT1215'

req = requests.get(requestUrl)

if req.status_code == 200:
    data = req.json()
    for d in data:  
        s = 'http://apidev.accuweather.com/currentconditions/v1/' + d['Key'] + '.json?language=en&apikey=hoArfRosT1215'        
        weather = requests.get(s)
        dataTwo = weather.json()
        for dTwo in dataTwo:
            print('It is ' + dTwo['WeatherText'] + ' outside.')
            print('Temp is: ' + str(dTwo['Temperature']['Imperial']['Value']))