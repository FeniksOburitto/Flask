from flask import Flask
app: Flask = Flask(__name__)


@app.route('/')
def index():
    return 'No hej '


@app.route('/<login>')
def login(login):
    return 'No hej {}'.format(login)


app.run(port=80,debug=True)
