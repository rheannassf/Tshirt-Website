from flask import Flask, render_template, request, url_for
app = Flask("MyApp")

@app.route("/tshirtresults")
def Load_Image_Text():
    text_description = "You're feeling fruity in this jazzy tee!"
    return render_template("tshirtresultpage.html", value=text_description)


app.run(debug=False)
