import requests

request = requests.get("http://weather-api:8000")
print("Status: {}".format(request.status_code))

print(request.json())