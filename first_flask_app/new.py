from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_page_rendering():
    return render_template("index.html")

@app.route("/about")
def about_page_rendering():
    name = "Nilankan"
    return render_template("about.html", name_show = name)

@app.route("/test")
def test_if_working():
    return "It (Flask) is working!"

app.run(debug=True)