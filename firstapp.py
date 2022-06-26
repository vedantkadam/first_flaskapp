from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/user/<name>')
def user(name):
    if name == 'home1':
        return redirect(url_for('home'))
    if name == 'student1':
        return redirect(url_for('about'))


if __name__ == "__main__":
    app.run(debug=True)
