import requests
from datetime import datetime

MY_LATITUDE = 51.507351  # Your latitude
MY_LONGITUDE = -0.127758  # Your longitude


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]

    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])

    #  Your position is within +5 or -5 degrees of the ISS position.
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    return (sunset <= time_now.hour < 24) or time_now.hour == 0 or (0 < time_now.hour <= sunrise)