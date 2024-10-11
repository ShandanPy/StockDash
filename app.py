from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
