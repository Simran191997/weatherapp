import requests  # Importing the requests library for API interactions


class WeatherApp:
    def __init__(self, api_key):
        """
        Initialize the WeatherApp instance with the API key.
        """
        self.api_key = api_key

    def fetch_weather_data(self, city):
        """
        weather_data variable will use the request
        library to go and fetch the url and whatever 
        resopnse it will get,will be contained in weather_data.
        Input: Name of a City.
        Response: Weather of the provided City.
        """
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={self.api_key}"
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # print(f"An error occurred while fetching data")
            return None

    def display_weather(self, city, unit):
        """
        Display the weather and temperature for the given city in the specified unit (Celsius or Fahrenheit).
        Input: 
         city:Name of a City.
         unit:Unit of the temperature,Celsius or Fahrenheit.
        Response: Weather of the provided City.
        """
        try:
            weather_data = self.fetch_weather_data(city)
            if not weather_data:
                return  # Exit if there was an error fetching data

            if weather_data['cod'] == '404':  # Error handling for invalid city
                print("City not found")
            else:
                # Extract weather and temperature
                weather = weather_data['weather'][0]['main']
                temp_celsius = weather_data['main']['temp']
                feels_like = weather_data['main']['feels_like']
                

                # Convert temperature to Fahrenheit if needed
                if unit == 'F':
                    temp = (temp_celsius * 9 / 5) + 32
                    temp_unit = "°F"
                else:
                    temp = temp_celsius
                    temp_unit = "°C"

                print(f"The weather in {city} is: {weather}")
                print(f"The temperature in {city} is: {temp}{temp_unit} and feels like {feels_like}{temp_unit}")
        except KeyError as e:
            print(f"Unexpected data format: missing key {e}")


# Main program
if __name__ == "__main__":
    # Read the API key from a file
    with open('api_key.txt', 'r') as file:
        api_key = file.read().strip()

    user_input = input('Enter the name of the city: ')
    # print(user_input)

    weather_app = WeatherApp(api_key)

    # Fetch weather data to check city validity
    weather_data = weather_app.fetch_weather_data(user_input)

    if not weather_data or weather_data.get('cod') == '404':
        print(f"The City {user_input} you have entered, doesn't exist. Exiting the program.")
    else:
        # Ask user for temperature unit preference
        while True:
            unit_choice = input("Would you like the temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()
            if unit_choice in ["C", "F"]:
                break
            else:
                print("Invalid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        # Display the weather in the chosen unit
        weather_app.display_weather(user_input, unit_choice)
