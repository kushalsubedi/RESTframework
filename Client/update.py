import requests
import json
URL="http://localhost:8000/api/update"
uid = "0c19cfc5-8b6c-4dfb-bb1a-76fca0df043f"
get_response = requests.patch(URL,json={
    "uid":uid,
    "title":"title by client",
    "description":"hello world from client"
    })


print (get_response.status_code)


print (get_response.json().values())