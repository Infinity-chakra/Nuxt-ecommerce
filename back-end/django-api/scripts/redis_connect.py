import redis

# Connect to Redis server (default host: 'localhost', default port: 6379)
try:
  r = redis.StrictRedis()
  # Ping the server to check connection
  pong = r.ping()
  if pong:
    print("Connected to Redis server!")
  else:
    print("Failed to connect to Redis server.")
except redis.exceptions.ConnectionError as e:
  print(f"Error connecting to Redis: {e}")

# Example usage (assuming successful connection)
name = "test_key"
value = "This is a test value"

# Set a key-value pair
r.set(name, value)

# Get the value for the key
get_value = r.get(name)

if get_value:
  print(f"Retrieved value for key '{name}': {get_value.decode('utf-8')}")  # Decode bytes to string
else:
  print(f"Key '{name}' not found.")

# Close the connection (optional)
r.close()