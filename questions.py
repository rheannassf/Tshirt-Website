from flask import Flask, render_template, request
app = Flask("answer")
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
    print result
    return result
app.run(debug=True)