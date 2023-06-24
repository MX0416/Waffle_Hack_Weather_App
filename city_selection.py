import requests

# Lat then Long
city_dict = {"Minneapolis" : [44.977489, -93.264374], "Seattle" : [47.6062, 122.3321], "New York" : [40.7128, 74.0060]}


def get_weather(long, lat):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=imperial&appid=1d21e89e8a54cc7271a3bb5c38934787"
    data = requests.get(url)
    result = data.json()

    #print(json.dumps(result, indent =4, sort_keys=True ))

    temp = result["main"]["temp"]
    humidity = result["main"]["humidity"]
    temp_max = result["main"]["temp_max"]
    temp_min = result["main"]["temp_min"]
    city_name = result["name"]
    description = result["weather"][0]["description"]
    feels_like = result["main"]["feels_like"]

    print(f"In {city_name} current temp is {temp} but it feels like {feels_like},")
    print(f"the humidity is {humidity} with the max temperature being {temp_max} and the low for the day being {temp_min},")
    print(f"the weather outside would be described as {description}!")