from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/blogs")
def blog_page():
    return render_template("blogs.html")

@app.route("/test")
def is_it_working():
    return "It's working!!"

app.run(debug=True)