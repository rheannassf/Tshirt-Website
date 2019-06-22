from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=["POST"])
def weather():
    request.form
    return render_template("main.html")

@app.route("/")
def index():
    return render_template

api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0f87c7a3d019cd7f75c37a68bcbcd073&q="
city = raw_input("City Name :")

url = api_address + city

json_data = requests.get(url).json()
formatted_data = json_data["weather"][0]["main"]

print(formatted_data)


