import requests

url = "https://api.thecatapi.com/v1/images/search"

response = requests.get(url)
print(response.text)

file = open("cat_img.txt", "a")
file.write(response.text)
file.close()

file = open("cat_img.txt", "r")
print(file.read())