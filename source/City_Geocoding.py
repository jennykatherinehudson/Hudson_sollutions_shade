import requests

class City_GeoCoding:
    def __init__(self, city, country_code):
        self.city = city
        self.country_code = country_code

    def city_geocoding(self):
        api_url = 'https://api.api-ninjas.com/v1/geocoding?city={}&country={}'.format(
            self.city, self.country_code)
        response = requests.get(
            api_url, headers={'X-Api-Key': '4qoS+6qOOEHn5DQjdd5+Jg==Z5LrsQM4npbJhtW6'})
        if response.status_code == requests.codes.ok:
            api_data = response.text.replace('[','').replace(']','').split('}')[0] + "}"
            return eval(api_data)
        else:
            print("Error:", response.status_code, response.text)


Krakow_name = 'Krakow'
Krakow_country = 'PL'
Krakow = City_GeoCoding(Krakow_name, Krakow_country).city_geocoding()

Sydney_name = 'Sydney'
Sydney_country = 'AU' 
Sydney = City_GeoCoding(Sydney_name, Sydney_country).city_geocoding()

NewYork_name = 'New York'
NewYork_country = 'USA'
NewYork = City_GeoCoding(NewYork_name, NewYork_country).city_geocoding()

Tokyo_name = 'Tokyo'
Tokyo_country = 'JP'
Tokyo = City_GeoCoding(Tokyo_name, Tokyo_country).city_geocoding()
