import requests
import json
URL="http://localhost:8000/api/create"

get_response = requests.post(URL,
                             json={
"title":"helloworld",
"description":"hello World is a beautifulmessage"
                                   })
print (get_response.text)

print (get_response.status_code)
print (get_response.json())