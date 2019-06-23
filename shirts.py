from flask import Flask, render_template, url_for
app = Flask("MyApp")

@app.route('/tshirtresultpage')
def tshirt_result():
    description = 'What a cool tshirt!'
    image='shirt1.jpeg'
    return render_template("tshirtresultpage.html", image=image, name='Your Shirt', description=description)

app.run(debug=True)
