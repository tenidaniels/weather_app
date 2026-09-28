# Weather App with Login & Registration

A simple Python desktop application built with **Tkinter** that allows users to register, log in, and check real-time weather information for any city using the **OpenWeatherMap API**.

## Features

- User registration
- User login authentication
- Password masking
- Search weather by city name
- Display:
  - Weather condition
  - Temperature (°C)
  - Humidity
  - Wind speed
- Error handling for invalid cities and network issues

## Technologies Used

- Python 3
- Tkinter (GUI)
- Requests (API calls)
- OpenWeatherMap API

## Project Structure

| Function | Purpose |
|----------|---------|
| `register()` | Creates a new user account. |
| `login()` | Authenticates registered users. |
| `get_weather()` | Retrieves weather data from OpenWeatherMap. |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-app-login.git
cd weather-app-login
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Get an OpenWeatherMap API Key

1. Create a free account at [OpenWeatherMap](https://openweathermap.org/api).
2. Generate an API key.
3. Replace the API key in the code:

```python
API_KEY = "YOUR_API_KEY"
```

### 4. Run the application

```bash
python weather_app.py
```

## How It Works

### Registration

- Enter a username.
- Enter a password.
- Click **Register**.
- The account is stored temporarily while the application is running.

### Login

- Enter your registered username and password.
- Click **Login**.
- After successful authentication, the Weather App screen opens.

### Weather Search

1. Enter a city name.
2. Click **Get Weather**.
3. The application displays:
   - City name
   - Weather description
   - Temperature
   - Humidity
   - Wind speed

## Example Output

```text
City: Lagos

Weather: scattered clouds
Temperature: 27°C
Humidity: 82%
Wind Speed: 3.5 m/s
```

## Error Handling

The application handles several common errors:

- Empty username or password
- Duplicate usernames
- Invalid login credentials
- Empty city input
- City not found
- Network connection errors

## Limitations

- User accounts are stored in memory and are lost when the application closes.
- Passwords are not encrypted.
- No database is used for persistent storage.

## Future Improvements

- Store users in a SQLite database.
- Encrypt passwords using hashing.
- Add a logout feature.
- Display weather icons.
- Show a 5-day weather forecast.
- Detect the user's current location automatically.
- Improve the interface with custom themes and icons.

## Python Concepts Demonstrated

- Functions
- Dictionaries
- GUI development with Tkinter
- Event-driven programming
- API integration with Requests
- Exception handling
- User input validation

## License

This project was created for educational purposes.
