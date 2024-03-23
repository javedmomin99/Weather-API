import requests

# Replace with your OpenWeatherMap API key
api_key = '22289792a7352c6cc75d9570ddc0d079' # Get yours from https://openweathermap.org/appid

places = [
    "London",
    "Paris",
    "Tokyo",
    "Sydney",
    "Rome",
    "Cairo",
    "Dubai",
    "Moscow",
    "Berlin",
    "Delhi",
    "Mumbai",
    "Beijing",
    "Toronto",
    "Barcelona",
    "Bangkok",
    "Istanbul",
    "Amsterdam",
    "New York",
    "Chicago",
    "Rio"
]


for city in places:
    # Define the API endpoint URL with the current city
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a GET request to the API
    response = requests.get(url)

    # Check for successful response (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Access and display weather information for the current city
        city_name = data["name"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        print(f"Weather in {city_name}: {temperature:.2f}°C, {description}")
    else:
        print(f"Error fetching weather data for {city}:", response.status_code)

