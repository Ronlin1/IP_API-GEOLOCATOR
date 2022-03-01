import requests
import json

# IP address to test
ip_address = '200.229.2.90'

# Our Endpoint (API) URL
request_url = f"https://geolocation-db.com/jsonp/{ip_address}"

# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()

# Clean the returned string so it just contains the JSON String
result = result.split("(")[1].strip(")")

# If you want to write to a file
with open("geo_one.json", "w+") as outfile:
    outfile.write(result)

# Convert this data into dictionary
result  = json.loads(result)
print(result)
