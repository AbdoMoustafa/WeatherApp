import requests as r
import datetime

import secrets

STORM_GLASS_END_POINT = "https://api.stormglass.io/v2"


def main():
    print("Hello")
    print(get_weather())


def check_secrets():
    storm_glass_url = "https://stormglass.io"


def get_weather():
    time = datetime.datetime.utcnow().replace(microsecond=0, second=0, minute=1)
    print(time)
    response = r.get(
        f"{STORM_GLASS_END_POINT}/weather/point",
        params={
            'lat': 58.7984,
            'lng': 17.8081,
            'params': {'airTemperature'},
            'start': {time},
            'end': {time}
        },
        headers={
            'Authorization': secrets.storm_glass_api_key
        }
    )
    return response.json()


if __name__ == '__main__':
    main()
