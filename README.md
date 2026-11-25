# Weather App

## Summary

Weather App is a desktop GUI application that retrieves current weather for a
city from the OpenWeatherMap Current Weather API. Enter a city name (optionally
with a country code, such as `Mumbai,IN`) and select **Find Weather** to view
the location coordinates, country, timezone, temperature in Celsius and
Fahrenheit, feels-like temperature in Celsius, pressure, humidity, visibility,
and wind information.
The window displays `weather.png` as its background and includes a button to
exit the application.

## Project Category

Python desktop application / graphical user interface (GUI), for looking up
current city weather.

## Tools Used

- **Python 3**
- **Tkinter** for the desktop interface (included with most Python
  installations)
- **Requests** for HTTP calls to the weather API
- **Pillow** for loading and resizing the background image
- **OpenWeatherMap Current Weather API** as the weather data source
- **`MY_OWM_API_KEY` environment variable** for the OpenWeatherMap API key

## Setup and Run

1. Register with [OpenWeatherMap](https://openweathermap.org/) and obtain an
   API key.
2. Set the key in the `MY_OWM_API_KEY` environment variable. For example, in
   PowerShell:

   ```powershell
   $env:MY_OWM_API_KEY = "your_api_key"
   ```

3. Install the project dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application from the project directory:

   ```bash
   python weather_app.py
   ```

Keep `weather.png` beside `weather_app.py` so the application can load its
background image.
