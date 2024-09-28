import folium
import pandas
import folium.features

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list (data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <3000:
        return"orange"
    else:
        return "red"



# Crear el mapa con OpenStreetMap (default)
map = folium.Map(
    location=[36.84705037806074, -2.4448177325102276], 
    zoom_start=6, 
    tiles="OpenStreetMap"  # Usa un tile diferente
)

# Crea un grupo de características
fg = folium.FeatureGroup(name="My Map")

# Añade marcadores a las coordenadas especificadas
for lt, ln, el in zip(lat,lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln, ], popup=str(el) + "m", icon=folium.Icon(color=color_producer(el))))

# Añade el grupo de características al mapa
map.add_child(fg)

# Guarda el mapa en un archivo HTML
map.save("Map1.html")
