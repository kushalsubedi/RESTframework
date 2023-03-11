import requests
import json
URL="http://localhost:8000/api"

get_response = requests.get(URL,json={})


print (get_response.status_code)


print (get_response.json())