#importar librerias
import requests

# 
# Leer la apiKey para la API
print('introduce la apiKey')
apiKey = input()

# 
#Manhattan, New York City, NY, USA (40.776676, -73.971321)
#Brooklyn, New York City, NY, USA (40.650002, -73.949997)
#Bronx, New York City, NY, USA (40.837048, -73.865433)
#Queens, New York City, NY, USA (40.742054, -73.769417)
#Staten Island, New York City, NY, USA (40.579021, -74.151535)

# 
# Seleccionar la region a descargar
print('Introduce la opcion de boroug')
option = input()
option = int(option)
name_file = ''
if option == 1:
    borough = '40.776676, -73.971321'
    name_file = 'manhatan1.json'
if option == 2:
    borough = '40.650002, -73.949997'
    name_file = 'brooklyn1.json'
if option == 3:
    borough = '40.837048, -73.865433'
    name_file = 'bronx1.json'
if option == 4:
    borough = '40.742054, -73.769417'
    name_file = 'queens1.json'
if option == 5:
    borough = '40.579021, -74.151535'
    name_file = 'state_island1.json'

# 
borough = borough.split(' ')

# 
url = "https://meteostat.p.rapidapi.com/point/hourly"

querystring = {"lat":borough[0],"lon":borough[1],"start":"2020-01-21","end":"2020-02-01","tz":"America/New_York","freq":"H"}

headers = {
	"X-RapidAPI-Key": apiKey,
	"X-RapidAPI-Host": "meteostat.p.rapidapi.com"
}

# 
# Hacer la llamada a la API
response = requests.request("GET", url, headers=headers, params=querystring)

# 
# Crear el json
file = open(name_file, 'w')
file.write(response.text)
file.close()

print('Hecho')




