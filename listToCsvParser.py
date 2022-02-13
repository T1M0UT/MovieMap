import re
import pandas as pd
from geopy import Nominatim

geo_locator = Nominatim(user_agent='my_request')
path_to_dataset = "locations.list"

with open(path_to_dataset, "r", encoding='utf-8', errors='ignore') as file:
    startRead = 14
    endRead = 1000
    listItems = file.read().splitlines()[startRead:]
    print(len(listItems))

    # newItems = []
    # for line in listItems:
    #     line = [x for x in line.split('\t') if x != '']
    #     # print(line)
    #     if len(line) < 2:
    #         continue
    #     result = re.findall(r'(\d{4})', line[0])
    #     if result:
    #         year = result[0]
    #     name = re.findall(r'\".*?\"', line[0])[0]
    #     location = line[1]
    #     # print(name, year, location)
    #     location = geo_locator.geocode(location)
    #     if not location:
    #         continue
    #     # print(location.latitude, location.longitude)
    #     newItems.append((name, year, location, location.latitude, location.longitude))
    # df = pd.DataFrame(newItems, columns=['Name', 'Year', 'Location', 'Latitude', 'Longitude'])
    # df.to_csv('locations.csv')
    #
