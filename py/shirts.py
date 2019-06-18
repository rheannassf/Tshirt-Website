from flask import Flask, render_template, request
app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("tshirtresultpage.html", image_path="../images/shirt1.jpeg", text_description="You're looking a little plain!")

app.run(debug=False)