import requests
import json

cityState = input("Enter the ciy, state you would like the weather for: ")

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