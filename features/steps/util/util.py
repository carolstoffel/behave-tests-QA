from geopy.geocoders import Nominatim


def get_city_by_lat_and_long(latitude, longitude):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    assert "address" in location.raw
    assert "city" in location.raw["address"]
    return location.raw["address"]["city"]