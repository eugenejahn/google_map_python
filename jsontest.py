import urllib, json
import pprint
import re
import requests
import sys




send_url = 'https://geoiptool.com'
r = requests.get(send_url)
j = json.loads(r.text)
lat = str(j['latitude'])
lon = str(j['longitude'])
print lat 
print lon 
print '\n'

destination = ''
for i in sys.argv[1:]:
	destination = destination + i 
URL2 = "https://maps.googleapis.com/maps/api/directions/json?mode=walking&origin=%s,%s&destination=%s&key=AIzaSyA1IwGCXckmkgbhZ5UVOYaS4eS6nUEkXTs"%(lat,lon,destination)


googleResponse = urllib.urlopen(URL2)
jsonResponse = json.loads(googleResponse.read())
# pprint.pprint(jsonResponse)

steps = jsonResponse['routes'][0]['legs'][0]['steps']

for i in range(len(steps)):
	distance     = steps[i]['distance']['text']
	times        = steps[i]['duration']['text']
	directions = steps[i]['html_instructions']
	print('Distance:' + distance +'\n')
	print('Times:' + times +'\n')
	Directions = ''
	no_skip = True
	for a in range(len(directions)): 
		if no_skip: 
			if directions[a] == '<':
				no_skip = False
			else:
				Directions = Directions + directions[a]
		elif directions[a] == '>':
			no_skip = True
			Directions = Directions + ' '	
	print('Directions:' + Directions +'\n')





