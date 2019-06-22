from flask import Flask, render_template, request, url_for
app = Flask("MyApp")

@app.route("/tshirtresults")
def Load_Image():
    text_description = "You're feeling fruity in this jazzy tee!"
    image_name = "shirt1.jpeg"
    return render_template("tshirtresultpage.html", image_name=image_name)


def index():
          generate_img("test.jpg"); #save inside static folder
          return '<img src=' + url_for('static',filename='test.jpg') + '>' 

app.run(debug=True)
