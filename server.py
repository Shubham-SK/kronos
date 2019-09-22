from flask import Flask, request, render_template, redirect
import os, subprocess, time

app = Flask(__name__)

@app.route('/stop')
def stop():
    # mosquitto_pub -d -t omnihacks -m \"record\"
    os.system("python publish.py")
    return render_template("STOP.html")

@app.route('/start')
def start():
    os.system("python stopublish.py")
    return render_template("START.html")

@app.route('/blood-pres')
def blood_pres():
    return redirect("http://io.adafruit.com/vishakh_arora29/feeds/blood-pressure")

@app.route('/heart-rate')
def heart_rate():
    return redirect("http://io.adafruit.com/vishakh_arora29/feeds/heart-rate")

@app.route('/')
def index():
    return render_template("START.html")


if __name__ == "__main__":
    app.run(debug=True)
