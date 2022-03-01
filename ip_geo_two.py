import requests
import json

# IP address to test
ip_address = '200.229.2.90'
access = "get_yours 🙂"

# Our Endpoint (API) URL
request_url = f"http://api.ipapi.com/api/{ip_address}?access_key={access}"

# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()

# If you want to write to a file
with open("geo_two.json", "w+") as outfile:
    outfile.write(result)

# Convert this data into dictionary
result  = json.loads(result)
print(result)
