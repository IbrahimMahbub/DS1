from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Weather data for 10 cities
WEATHER_DATA = {
    "New York": "Sunny, 25°C",
    "Los Angeles": "Cloudy, 20°C",
    "Chicago": "Rainy, 15°C",
    "Houston": "Sunny, 30°C",
    "Phoenix": "Hot, 35°C",
    "Philadelphia": "Windy, 18°C",
    "San Antonio": "Stormy, 22°C",
    "San Diego": "Mild, 24°C",
    "Dallas": "Humid, 27°C",
    "San Jose": "Cool, 19°C"
}

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8080), requestHandler=RequestHandler)
server.register_introspection_functions()

# Define method to get weather data
def get_weather(cities):
    result = {}
    for city in cities:
        if city in WEATHER_DATA:
            result[city] = WEATHER_DATA[city]
        else:
            result[city] = "No data available"
    return result

# Register function with the server
server.register_function(get_weather, "get_weather")

print("Weather RPC Server is running on port 8080...")
server.serve_forever()
