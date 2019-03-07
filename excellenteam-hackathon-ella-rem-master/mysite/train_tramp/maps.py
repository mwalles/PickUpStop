import folium
import base64
import qrcode
from io import BytesIO
from .paths import *
from .models import Person
from geopy.geocoders import Nominatim
from time import sleep


def get_lot_lat(address):
    geolocator = Nominatim(user_agent="my_site")
    location = geolocator.geocode(address)
    return [location.latitude, location.longitude]


def generate_map(next_stop):
    print(next_stop)
    stop_name, stop_location = list(path_1.items())[next_stop]
    map_osm = folium.Map(location=[stop_location[1], stop_location[0]], zoom_start=15)

    for key, location in path_1.items():
        folium.CircleMarker(
            location=[location[1], location[0]],
            radius=20,
            popup="train station",
            color='red',
            fill=True,
            fill_color='red'
        ).add_to(map_osm)

    all_person = Person.objects.all()

    for item in all_person:
        if item.destination != stop_name:
            continue

        url = f"https://33fad170.ngrok.io/id/{item.id}"
        img = qrcode.make(url, box_size=2)

        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())

        f = f'<img src="data:image/png;base64,{img_str}">'
        f = f.replace("""b\'""", "")
        f = f.replace("""==""", "")
        f = f.replace("""\'""", "")

        address = item.street
        address += ' '
        address += str(item.num)
        address += ' '
        address += item.city

        folium.CircleMarker(
            location=get_lot_lat(address),
            radius=3,
            popup=folium.Popup(f, show=True),
            color='black'
        ).add_to(map_osm)

    return map_osm


if __name__ == "__main__":
    generate_map(6).save('stamen_toner.html')
