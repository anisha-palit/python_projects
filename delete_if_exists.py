import requests
import os

url = "https://api.thecatapi.com/v1/images/search"

response = requests.get(url)
print(response.text)

if os.path.exists("cat_img.txt"):
  os.remove("cat_img.txt")
else:
  print("The file does not exist")