import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles = "Mapbox Bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, na in zip(lat, lon, elev, name):
    fgv.add_child(folium.features.CircleMarker(location = [lt,ln], radius = 5, fill = True, popup = folium.Popup(str(na) + " " + str(el), parse_html=True), color = color_producer(el)))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open("world.json", "r", encoding="UTF-8-sig").read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")
