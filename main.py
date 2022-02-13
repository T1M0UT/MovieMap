from math import sin, atan2, cos, sqrt, pi

import pandas as pd
import haversine
from geopy import Nominatim
import folium


geo_locator = Nominatim(user_agent='my_request')

myLatitude = 49.83826
myLongitude = 24.02324

path_to_dataset = "locations.csv"


def color_creator(distance):
    if distance < 10_000:
        return "green"
    elif distance <= 100_000:
        return "yellow"
    else:
        return "red"


df = pd.read_csv(path_to_dataset)
distances = []
for index, row in df.iterrows():
    lat1 = row['Latitude']
    lon1 = row['Longitude']
    R = 6371e3  # metres
    φ1 = lat1 * pi / 180  # φ, λ in radians
    φ2 = myLatitude * pi / 180
    dφ = (myLatitude - lat1) * pi / 180
    dλ = (myLongitude - lon1) * pi / 180
    if row["Name"] == "2012 UEFA European Football Championship":
        print("AAAAAA")
    if row["Name"] == "1001 Things You Should Know":
        print("BBBBBBB\n\n")
    a = sin(dφ / 2) * sin(dφ / 2) + cos(φ1) * cos(φ2) * sin(dλ / 2) * sin(dλ / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    d = R * c  # in metres
    distances.append((d, lat1, lon1, row['Name']))
distances = list(dict.fromkeys(distances))
distances.sort(key=lambda x: x[0])
map = folium.Map(location=[myLatitude, myLongitude], zoom_start=10)
map.add_child(folium.Marker(location=[myLatitude, myLongitude],
                            popup="You are here!",
                            icon=folium.Icon()))
fg = folium.FeatureGroup(name="Movies")
for d, lat, long, name in distances[:15]:
    fg.add_child(folium.CircleMarker(location=[lat, long],
                               radius=10,
                               popup=name,
                               fill_color=color_creator(d),
                               color="grey",
                               fill_opacity=0.5,))
    print(name, lat, long)
map.add_child(fg)
map.save('Map_5.html')

# print(distances[:10])
# print(df)

