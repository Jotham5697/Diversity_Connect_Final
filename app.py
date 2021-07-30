from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def test3():
    return render_template("index.html")

@app.route("/podcasts")
def podcasts():
    return render_template("/podcasts.html")

@app.route("/chat")
def chat():
    return render_template("/chat.html")

@app.route("/resources")
def resources():
    return render_template("/resources.html")