import requests
import json 


api_url = "https://api-dbw.stat.gov.pl/api/1.1.0/area/area-area"
response = requests.get(api_url)



data = response.json()



print("--- FIRST 3 ITEMS IN THE DATA ---")
print(json.dumps(data[:3], indent=4)) 


print("\nTotal number of items received:", len(data))