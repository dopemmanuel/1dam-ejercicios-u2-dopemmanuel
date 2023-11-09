import geocoder

location = geocoder.ip('me')

if location.latlng:
    lat, lng = location.latlng
    print("Ubicación actual (latitud, longitud): ", lat, lng)
else:
    print("No se pudo determinar la ubicación.")
