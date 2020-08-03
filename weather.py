import requests, json
def weather(CITY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "f35c2d69bbee6d24283a58acbbb7219a"
    # upadting the URL
    URL = f"{BASE_URL}q={CITY}&appid={API_KEY}&units=metric"
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        # showing the error message
        print("Error in the HTTP request")
        print(response.status_code)
