from flask import Flask, request, render_template, redirect
import os, subprocess, time
import TranscriptGeneration.adafruitmetrics as adafruit
import TranscriptGeneration.transcriptcreate as transcript

app = Flask(__name__)

@app.route('/stop')
def stop():
    # mosquitto_pub -d -t omnihacks -m \"record\"
    os.system("python publish.py")
    return render_template("STOP.html")

@app.route('/start')
def start():
    os.system("python stopublish.py")
    print("generating transcript")
    global blood_pressure, heart_rate
    # metrics = os.system("python TranscriptGeneration/transcript_create.py")
    metrics = transcript.main()
    print(type(metrics), len(metrics))
    blood_pressure = metrics[0]
    heart_rate = metrics[1]
    print("done generating transcript")
    return render_template("START.html")

@app.route('/blood-pres')
def blood_pres():
    adafruit.blood_publish(blood_pressure)
    return redirect("http://io.adafruit.com/vishakh_arora29/feeds/blood-pressure")

@app.route('/transcript')
def transcript():
    fin = open("transcript.txt","r")
    return fin.read()

@app.route('/heart-rate')
def heart_rate():
    adafruit.heart_publish(heart_rate)
    return redirect("http://io.adafruit.com/vishakh_arora29/feeds/heart-rate")

@app.route('/')
def index():
    return render_template("START.html")

if __name__ == "__main__":
    app.run(debug=True)
