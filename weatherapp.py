import tkinter as tk
from tkinter import messagebox
import requests



API_KEY= "30b9ea1d7ffaa3c62201a9aa1bed9e31"

users= {}

# Registration
def register():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning(
            "Warning",
            "Username and password cannot be empty"
        )
        return

    if username in users:
        messagebox.showerror(
            "Error",
            "Username already exists"
        )
        return

    users[username] = password
    messagebox.showinfo(
        "Success",
        f"User {username} registered successfully"
    )

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Login
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if users.get(username) == password:
        messagebox.showinfo(
            "Login Success",
            f"Welcome, {username}"
        )

        login_frame.pack_forget()
        weather_frame.pack(pady=20)

    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )


# Weather App
def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Warning",
            "Please enter a city name"
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            result_label.config(text="City not found")
            return

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (
            f"City: {city}\n\n"
            f"Weather: {weather}\n"
            f"Temperature: {temp} °C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )

        result_label.config(text=result)

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Network Error",
            "Unable to connect to the weather service."
        )


# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("450x350")


# Login/Register Frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(
    login_frame,
    text="Username:"
).grid(row=0, column=0, sticky="e")

username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(
    login_frame,
    text="Password:"
).grid(row=1, column=0, sticky="e")

password_entry = tk.Entry(
    login_frame,
    show="*"
)
password_entry.grid(row=1, column=1, padx=5, pady=5)

register_btn = tk.Button(
    login_frame,
    text="Register",
    command=register
)
register_btn.grid(row=2, column=0, pady=10)

login_btn = tk.Button(
    login_frame,
    text="Login",
    command=login
)
login_btn.grid(row=2, column=1, pady=10)


# Weather Frame
weather_frame = tk.Frame(root)

title = tk.Label(
    weather_frame,
    text="Weather App",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

city_entry = tk.Entry(weather_frame, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(
    weather_frame,
    text="Get Weather",
    command=get_weather
)
search_btn.pack(pady=10)

result_label = tk.Label(
    weather_frame,
    text="",
    justify="left"
)
result_label.pack(pady=20)

root.mainloop()























