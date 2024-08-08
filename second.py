from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/second")
def second():
    try:
        line = input()
        return line
    except:
        return "[done]"


app.run(host="127.0.0.1", port=3469)
