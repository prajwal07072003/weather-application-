import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

def get_weather():
    city = city_entry.get()
    api_key = '30d4741c779ba94c470ca1f63045390a'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '404':
        messagebox.showerror("Error", "City not found")
    else:
        weather = data['weather'][0]['main']
        temp = round(data['main']['temp'])
        weather_label.config(text=f"Weather: {weather}", fg="white", bg="sky blue", font=("Helvetica", 16))
        temp_label.config(text=f"Temperature: {temp}°C", fg="white", bg="sky blue", font=("Helvetica", 16))

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Apply custom theme
style = ThemedStyle(root)
style.theme_use("clam")

# Load and resize the weather icon
icon_url = "https://openweathermap.org/img/wn/"
weather_icon = Image.open("D:\python project\wheather app\icon.jpeg")  # Default icon if no icon is fetched
weather_icon = ImageTk.PhotoImage(weather_icon.resize((100, 100)))

# Create and place widgets
city_label = tk.Label(root, text="Enter city:", font=("Helvetica", 20))
city_label.grid(row=0, column=0, padx=20, pady=20)

city_entry = tk.Entry(root, font=("Helvetica", 20))
city_entry.grid(row=0, column=1, padx=20, pady=20)

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 20), command=get_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

weather_label = tk.Label(root, text="", font=("Helvetica", 20))
weather_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

temp_label = tk.Label(root, text="", font=("Helvetica", 20))
temp_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

# Run the main event loop
root.mainloop()
