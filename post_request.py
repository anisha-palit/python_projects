import requests
import json

url = "https://api.thecatapi.com/v1/votes"
api_key = "live_vOKRL9EqmSUi5h62KH3dlaC8n6gR3RWUtMLu5i2X1ZJnfuWJkPPvyWOoYJP9RTXS"
headers = {"x-api-key": api_key}

data = {
    "image_id":"2bbSbBC-v",
    "sub_id":"demo-474a90",
    "value": 1
}

response = requests.post(url = url, json = data, headers = headers)
status_code = response.status_code

if (status_code == 201):
    print(" Status code : 201 ; Successful POST request ")
    print(response.text)
else:
    print(status_code)
    print(response.text)

