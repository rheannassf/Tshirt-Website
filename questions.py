from flask import Flask, render_template, request
app = Flask("MyApp")


@app.route("/answer")
def loadquestions():
    return render_template("questions.html")


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
        description = 'What..... tshirt!'
        image='shirt2.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)
    if result == "101":
        description = 'What..... tshirt!'
        image='shirt4.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)
    else:
        description = 'What..... tshirt!'
        image='shirt6.jpg'
        return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)

app.run(debug=True)
