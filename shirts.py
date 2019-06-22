from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/tshirtresultpage')
def show_image():
    full_filename = ('images/'+'shirt1.jpeg')
    return render_template("tshirtresultpage.html", image = full_filename)
app.run(debug=True)
