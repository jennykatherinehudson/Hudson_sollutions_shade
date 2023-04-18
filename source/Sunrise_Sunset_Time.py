import requests
import json

class Sunrise_Sunset_Time:
    def __init__(self, city_lat, city_lng, date):
        self.city_lat = city_lat
        self.city_lng = city_lng
        self.date = date

    def sunrise_sunset_time(self):
        api_url = 'https://api.sunrisesunset.io/json?lat={}&lng={}&date={}'.format(
            self.city_lat,self.city_lng, self.date)
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            api_data = response.text.replace('{"results":', "").split(',"status"')[0]
            return json.loads(api_data)
        else:
            print("Error:", response.status_code, response.text)



