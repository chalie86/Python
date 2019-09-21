import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])




#map = folium.Map(location=[lon, lat], zoom_start=6, tiles="Stamen Terrain")
map = folium.Map(location=[0, 0], zoom_start=6)



fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
     fg.add_child(folium.Marker(location=[lt, ln],popup=str(el),icon=folium.Icon(color='green')))
	
map.add_child(fg)

map.save("map99.html")	