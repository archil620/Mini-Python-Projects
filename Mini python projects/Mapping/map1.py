import folium
import pandas

data= pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
ele=list(data["ELEV"])

def color_changer(elevation):
    if elevation< 1000:
        return'green'
    elif 1000<=elevation <3000:
        return 'orange'
    else:
        return'red'




map = folium.Map(location=[44.648866, -63.579223], zoom_start = 13)

fg= folium.FeatureGroup(name="My Map")
fgv=folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon, ele):
     fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6,popup=str(el),fill=True,fill_color=color_changer(el),fill_opacity=0.7))

fg.add_child(folium.Marker(location=[44.643048, -63.574880],popup="Hi I live here",icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[44.637532, -63.586699],popup="Hi I study here",icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=[44.649478, -63.618242],popup="Hi I work here",icon=folium.Icon(color="blue")))

fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']< 10000000
else 'orange'if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fg)
map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")