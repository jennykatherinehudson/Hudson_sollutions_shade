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


Krakow = City_GeoCoding('Krakow', 'PL').city_geocoding()

Sydney = City_GeoCoding('Sydney', 'AU').city_geocoding()

NewYork = City_GeoCoding('New York', 'USA').city_geocoding()

Tokyo = City_GeoCoding('Tokyo', 'JP').city_geocoding()
