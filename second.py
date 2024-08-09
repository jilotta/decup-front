from flask import Flask
from flask_cors import CORS, cross_origin
from os import _exit

done = False
app = Flask(__name__)
CORS(app)

@app.route("/second")
def second():
    print("HIT")
    global done
    if done:
        print(done)
        _exit(0)
    try:
        line = input()
        if line == "[done]":
            raise ValueError
        return line
    except:
        done = True
        return "[done]"

@app.route("/done")
def quit():
    exit(0)

app.run(host="127.0.0.1", port=3469)
