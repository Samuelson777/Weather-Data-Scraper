''' Weather Data Scraper

Objective: Scrape weather data from a website to collect and display current weather information for a specific location.

Tools and Technologies:
Programming Language: Python

Libraries:
requests for making HTTP requests
BeautifulSoup for parsing HTML
pandas (optional) for data manipulation and storage '''

import requests

# Function to get weather data
def get_weather(city, api_key):
    # URL of the OpenWeatherMap API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None, None
    
    # Parse the JSON response
    data = response.json()
    
    # Extract weather information
    temperature = data['main']['temp']
    condition = data['weather'][0]['description']
    
    return temperature, condition

# Main function
if __name__ == "__main__":
    city = "Chennai"  # Replace with your desired city
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    temperature, condition = get_weather(city, api_key)
    if temperature is not None and condition is not None:
        print(f"The current temperature in {city} is {temperature}°C with {condition}.")