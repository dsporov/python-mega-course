import folium

#print map, type(map)
fg = folium.FeatureGroup(name = "My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi, I am a marker", icon=folium.Icon(color='green')))

map = folium.Map(location=[38.2, -99.1])
map.add_child(fg)
map.save("map1.html")
