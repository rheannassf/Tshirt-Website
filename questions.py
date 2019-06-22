from flask import Flask, render_template, request
app = Flask("MyApp")
@app.route("/answer", methods=["POST"])
def answer():
form_data = request.form
