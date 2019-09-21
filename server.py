from flask import Flask, request, render_template

main_page = """
<!DOCTYPE html>
<html>
<body>

<h2>Button</h2>
<form action="button">
    <button type="submit">Press Button!</button>
<form>

</body>
</html>
"""

app = Flask(__name__)

@app.route('/button')
def button():
    print("Hello World")
    return main_page

@app.route('/')
def index():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
