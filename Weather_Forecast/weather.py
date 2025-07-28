import os
from dotenv import load_dotenv
import requests
load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("Error: API_KEY not found in environment variables.")
    exit(1)

def get_weather_data(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {city_name} is likely to be {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Min Temperature: {data['main']['temp_min']}°C")
        print(f"Max Temperature: {data['main']['temp_max']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Visibility: {data['visibility']} m")
        print(f"Cloudiness: {data['clouds']['all']}%")
    else:
        print(f"Error: {response.status_code} - {response.text}")    

def check_again():
    choice = input("\nDo you want to check the weather for another city? (yes/no): ").strip().lower()
    if choice == 'yes':
        city_name = input("Enter the city name: ")
        get_weather_data(city_name)
        check_again()
    else:
        print("Exiting the program.")
        exit(0)

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    get_weather_data(city_name)
    check_again()        