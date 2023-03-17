with open("city_geocoding.txt", "r") as file:
    data = file.read()
    data = data.replace('[', "")
    data = data.replace(']', ",")
    cities = eval(data[:-1])

Cities = []
Krakow = None
Sydney = None
NewYork = None
Tokyo = None
for cities in cities:
    if cities['name'] == "Krakow":
        Krakow = cities
        Cities.append(Krakow)
    if cities['name'] == "Sydney":
        Sydney = cities
        Cities.append(Sydney)
    if cities['name'] == "New York":
        NewYork = cities
        Cities.append(NewYork)
    if cities['name'] == "Tokyo":
        Tokyo = cities
        Cities.append(Tokyo)
 
print(Cities)
