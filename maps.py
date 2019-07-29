import urllib.parse

def get_url():

    location = [
        {"lat": 41.0082, "long": 28.9784},
        {"lat": 36.8571, "long": 28.2692},
        {"lat": 41.0027, "long": 39.7168},
        {"lat": 28.4904, "long": 39.6540}]

    param={"access_token":"pk.eyJ1IjoiYXNsaW96IiwiYSI6ImNqeWg1eWZ2NjA4ZnQzbHFneTJrczVncGMifQ.Fppu9PCPDS1E8Jqf3bjbzA"}

    encoded = urllib.parse.urlencode(param)

    base_url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{0}/auto/500x300?" + encoded


    location_list = []

    for point in location:
        value = "pin-s-a+9ed4bd({0},{1})".format(point["long"], point["lat"])

        location_list.append(value)

    location_values = ",".join(location_list)

    formated_url = base_url.format(location_values)


    return formated_url

