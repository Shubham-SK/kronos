from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/start')
def start():
    print("Hello World")
    return render_template("START.html")
    

@app.route('/stop')
def stop():
    os.system("mosquitto_pub -d -t omnihacks -m \"record\"")
    return render_template("STOP.html")

@app.route('/')
def index():
    return render_template("START.html")    

  


if __name__ == "__main__":
    app.run(debug=True)
