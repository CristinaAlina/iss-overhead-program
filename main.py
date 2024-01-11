import requests

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
