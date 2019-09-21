from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/button')
def button():
    print("Hello World")
    return render_template("STOP.html")
    

@app.route('/')
def index():
    return render_template("START.html")

if __name__ == "__main__":
    app.run(debug=True)
