import requests
import tkinter as tk
from tkinter import messagebox

class WeatherForecast:
    API_KEY = '29bd1210377d20451e20e0fd6e6b337a'

    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast")

        # Configure rows and columns
        for i in range(6):
            self.root.rowconfigure(i, minsize=100)
        for i in range(4):
            self.root.columnconfigure(i, minsize=200)

        label_font = ("Helvetica", 16)

        location_label = tk.Label(root, text="Location:", font=label_font)
        location_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.temperature_display = tk.Label(root, text="", font=label_font)
        self.temperature_display.grid(row=1, column=0, padx=5, pady=5, sticky="we")

        self.humidity_display = tk.Label(root, text="", font=label_font)
        self.humidity_display.grid(row=2, column=0, padx=5, pady=5, sticky="we")

        self.wind_speed_display = tk.Label(root, text="", font=label_font)
        self.wind_speed_display.grid(row=3, column=0, padx=5, pady=5, sticky="we")

        self.pressure_display = tk.Label(root, text="", font=label_font)
        self.pressure_display.grid(row=4, column=0, padx=5, pady=5, sticky="we")

        self.precipitation_display = tk.Label(root, text="", font=label_font)
        self.precipitation_display.grid(row=5, column=0, padx=5, pady=5, sticky="we")

        self.text_input_field = tk.Entry(root, width=15)
        self.text_input_field.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        get_text_button = tk.Button(root, text="Search", command=self.get_weather_data)
        get_text_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")

    def get_weather_data(self):
        city_name = self.text_input_field.get().capitalize()
        if not city_name:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        weather_data = self.fetch_weather_data(city_name)
        if weather_data:
            self.update_weather_labels(weather_data)
        else:
            messagebox.showerror("Error", f"Unable to get weather forecast for {city_name}")

    def fetch_weather_data(self, city_name):
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={self.API_KEY}"
        response = requests.get(base_url)
        data = response.json()

        if 'main' in data:
            weather_details = {
                "temperature": data['main'].get('temp', 'N/A'),
                "humidity": data['main'].get('humidity', 'N/A'),
                "pressure": data['main'].get('pressure', 'N/A'),
                "wind_speed": data['wind'].get('speed', 'N/A'),
                "precipitation": data['rain'].get('1h', 'N/A') if 'rain' in data else 'N/A'
            }
            return weather_details
        else:
            messagebox.showerror("Error", f"Error: {data.get('message', 'Unknown error')}")
            return None

    def update_weather_labels(self, weather_data):
        self.temperature_display.config(text=f"Temperature: {weather_data['temperature']} °C")
        self.humidity_display.config(text=f"Humidity: {weather_data['humidity']}%")
        self.wind_speed_display.config(text=f"Wind Speed: {weather_data['wind_speed']} m/s")
        self.pressure_display.config(text=f"Pressure: {weather_data['pressure']} hPa")
        self.precipitation_display.config(text=f"Precipitation: {weather_data['precipitation']} mm")


if __name__ == "__main__":
    root = tk.Tk()
    weather_forecast = WeatherForecast(root)
    root.mainloop()
