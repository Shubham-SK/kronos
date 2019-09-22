from flask import Flask, request, render_template
import os, subprocess, time

app = Flask(__name__)

@app.route('/stop')
def stop():
    # mosquitto_pub -d -t omnihacks -m \"record\"
    global f_kill
    f_kill = subprocess.Popen(["python", "record_audio.py"])
    return render_template("STOP.html")

@app.route('/start')
def start():
    f_kill.terminate()
    return render_template("START.html")
    



@app.route('/')
def index():
    return render_template("START.html")    

  


if __name__ == "__main__":
    app.run(debug=True)
