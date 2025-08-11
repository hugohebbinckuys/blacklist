from flask import Flask

app = Flask(__name__)

app.route('/')
def test() : 
    return "Yo test réussi"

if __name__ == '__main__' : 
    app.run(host='0.0.0.0', port=500, debug=True)