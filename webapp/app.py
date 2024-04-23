from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    matches=[]
    if request.method=="POST":
        text = request.form.get("text")
        patterns = request.form.get("patterns")
        matches = re.findall(patterns, text)
    return render_template("home.html", matches=matches)

def emails(email):
        patterns = r"[0-9a-zA-Z_]+@[a-zA-z]+\.[a-zA-Z.]+"
        return re.findall(patterns, email)

@app.route('/email', methods=["POST"])
def validate():
    email = request.form['email']
    if emails(email):
        return render_template('email_valid.html', email=email)
    else:
        return render_template('email_invalid.html', email=email)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",)