from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/weather", methods=["POST"])
def weather():
    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0f87c7a3d019cd7f75c37a68bcbcd073&q="
    city = request.form['city']

    url = api_address + city

    json_data = requests.get(url).json()
    formatted_data = json_data["weather"][0]["main"]
    return render_template("index.html", weather=formatted_data)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/questions")
def questions():
    return render_template('questions.html')

@app.route("/answer", methods=["POST"])
def answer():
    form_data = request.form['purpose']
    return form_data

@app.route('/tshirtresultpage', methods=["POST"])
def response():
    form_data = request.form
    radioval = (form_data["purpose"])
    radioval1 = (form_data["purpose1"])
    radioval2 = (form_data["purpose2"])
    result = radioval + radioval1 + radioval2
    if result == "111":
        description = 'What a cool tshirt!'
        image='shirt1.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)
    if result == "011":
        description = 'What a risky tshirt!'
        image='shirt3.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)
    if result == "100":
        description = 'What a great tshirt!'
        image='shirt2.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)
    if result == "101":
        description = 'What a snazzy tshirt!'
        image='shirt4.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)
    else:
        description = 'What groovy tshirt!'
        image='shirt6.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)






