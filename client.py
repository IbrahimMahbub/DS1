import xmlrpc.client

# Connect to the RPC server
server = xmlrpc.client.ServerProxy("http://localhost:8080/RPC2")

# Request weather data for specific cities
cities = ["New York", "Chicago", "San Diego", "Seattle"]
weather_info = server.get_weather(cities)

# Display the results
for city, weather in weather_info.items():
    print(f"{city}: {weather}")
