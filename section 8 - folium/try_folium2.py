import folium
import pandas
import json
import io

data = pandas.read_csv('app2-web-map/Volcanoes.txt')
lat = list(data.LAT)
lon = list(data.LON)
elev = list(data['ELEV'])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def colorOfElevation(elev):
  if elev < 1000:
    return 'green'
  elif elev < 3000:
    return 'orange'
  else:
      return 'red'

fg = folium.FeatureGroup(name = "My Map")
# for lt, ln, el, name in zip(lat,lon, elev, name):
# #  fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el) + ' m'), icon=folium.Icon(color='green')))
#   iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
#   fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=colorOfElevation(el))))

for lt, ln, el, name in zip(lat,lon, elev, name):
  iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
  fg.add_child(
      folium.CircleMarker(
        location=[lt, ln],
        radius=6,
        popup=folium.Popup(iframe),
        fill_color=colorOfElevation(el),
        fill=True,
        color = 'grey',
        fill_opacity=0.7)
    )

map = folium.Map(location=[38.58, -99.1], zoom_start=6, tiles="Mapbox Bright")

map.add_child(fg)

f = io.open('app2-web-map/world.json', 'r', encoding='utf-8-sig')
world = json.load(f)
f.close()

print type(world)
map.add_child(folium.GeoJson(data=world,
  style_function = lambda x: {'fillColor':
       'green' if x['properties']['POP2005'] < 10000000
  else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
  else 'red'} ))

map.add_child(folium.LayerControl())

map.save("map1.html")
