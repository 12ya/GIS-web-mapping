import folium
import os

#geojson
overlay = os.path.join('data', 'overlay.json')
#creating map

m = folium.Map(location = [35.9078, 127.7669], zoom_start = 8)


tooltip = 'click for more'

folium.Marker([35.1796, 129.0756],   
                          popup = '<elegant>the Best city in Korea</elegant>',
                          tooltip = tooltip).add_to(m)



#circle marker

folium.CircleMarker(
    location = [36.024516 ,129.361592],
    radius = 35,
    color = '#6a0dad',
    fill = True,
    fill_color = '#6a0dad'


).add_to(m)

#generating json
folium.GeoJson(overlay, name = 'FRIEND').add_to(m)

folium.Marker([35.1595, 126.8526],
               popup = 'Nikita',
               tooltip = 'close one').add_to(m)

#generating map

m.save("map.html")