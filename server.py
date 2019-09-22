from flask import Flask, request, render_template
import os, subprocess, time

app = Flask(__name__)

@app.route('/stop')
def stop():
    # mosquitto_pub -d -t omnihacks -m \"record\"
    os.system("python publish.py")
    return render_template("STOP.html")

@app.route('/start')
def start():
#    os.system("python mqtt.py")
    os.system("python stopublish.py")
    return render_template("START.html")
    



@app.route('/')
def index():

    return render_template("START.html")    

  


if __name__ == "__main__":
    app.run(debug=True)
