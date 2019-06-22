import requests
from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/<weather>")
def main(weather):
    return render_template("main.html", weather=name.title())

api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0f87c7a3d019cd7f75c37a68bcbcd073&q="
city = raw_input("City Name :")

url = api_address + city

json_data = requests.get(url).json()
formatted_data = json_data["weather"][0]["main"]

print(formatted_data)

