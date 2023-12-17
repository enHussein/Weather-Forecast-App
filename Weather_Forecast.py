# Register on openweathermap and get API key
# Import requests
import requests
import tkinter as tk

class WeatherForecast:
    api_key = '29bd1210377d20451e20e0fd6e6b337a'  # Replace this with your actual API key
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Weather Forecast")  # Set the window title

        # Configure rows and columns
        for i in range(6):
            self.root.rowconfigure(i, minsize=100)
        for i in range(4):
            self.root.columnconfigure(i, minsize=200)

        # Create a label with a larger font size
        label_font = ("Helvetica", 16)  # Specify the font family and size

        # Create a label for text input field
        location_label = tk.Label(root, text="Location:", font=label_font)
        location_label.grid(row=0, column=1, padx=10, pady=10, sticky="e")
    

        # Create labels for displaying weather details

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
        

        # Create an entry widget for text input
        self.text_input_field = tk.Entry(root, width=15)
        self.text_input_field.grid(row=0, column=2, padx=10, pady=10, sticky="w")

       # Create a button to get text from the Text Input Field
        get_text_button = tk.Button(root, text="Search", command=self.get_text_from_entry)
        get_text_button.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        # Initialize dictionaries to store weather details
        self.weather_details = {
            "temperature": tk.StringVar(),
            "humidity": tk.StringVar(),
            "wind_speed": tk.StringVar(),
            "pressure": tk.StringVar(),
            "precipitation": tk.StringVar()}

    def get_text_from_entry(self):
        # Fetch the text from the Text Input Field
        proposedcity = self.text_input_field.get()
        weather_data = self.get_weather_forecast(proposedcity)
        if weather_data:
            print(f"Weather Forecast for {proposedcity}: {weather_data}")
            # Update labels with weather details
            self.weather_details["temperature"].set(f"Temperature: {weather_data['temperature']} °C")
            self.weather_details["humidity"].set(f"Humidity: {weather_data['humidity']}%")
            self.weather_details["wind_speed"].set(f"Wind Speed: {weather_data['wind_speed']} m/s")
            self.weather_details["pressure"].set(f"Pressure: {weather_data['pressure']} hPa")
            self.weather_details["precipitation"].set(f"Precipitation: {weather_data['precipitation']} mm")
        else:
            print(f"Unable to get weather forecast for {proposedcity}")
        # Update labels with weather details    
        self.temperature_display.config(text=f"Temperature: {weather_data['temperature']} °C")
        self.humidity_display.config(text=f"Humidity: {weather_data['humidity']}%")
        self.wind_speed_display.config(text=f"Wind Speed: {weather_data['wind_speed']} m/s")
        self.pressure_display.config(text=f"Pressure: {weather_data['pressure']} hPa")
        self.precipitation_display.config(text=f"Precipitation: {weather_data['precipitation']} mm")

    def get_weather_forecast(self,city_name):
        
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={self.api_key}"

        response = requests.get(base_url)
        data = response.json()
       # print("API Response:", data)  # Print the entire API response for debugging

        if 'main' in data:
            weather_details = {
                "temperature": data['main'].get('temp', 'N/A'),
                "humidity": data['main'].get('humidity', 'N/A'),
                "pressure": data['main'].get('pressure', 'N/A'),
            }
            if 'wind' in data and 'speed' in data['wind']:
                weather_details["wind_speed"] = data['wind']['speed']
            else:
                weather_details["wind_speed"] = 'N/A'

            if 'rain' in data and '1h' in data['rain']:
                weather_details["precipitation"] = data['rain']['1h']
            else:
                weather_details["precipitation"] = 'N/A'
            
            return weather_details
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None


    

    

if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()

    # Create an instance of the WeatherForecast class
    weather_forecast = WeatherForecast(root)

    # Start the Tkinter main loop
    root.mainloop()
