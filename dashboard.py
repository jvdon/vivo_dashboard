from flask import Flask, request, jsonify, make_response

import utils

app = Flask(__name__, static_url_path="/static")


@app.get("/")
def index():
    return "<h1>Hello World</h1>"


@app.get("/ping/<server>")
def ping(server: str):
    respTime, status = utils.ping(server)
    ok = (status == True)
    response = jsonify({
        "status": "Ok" if ok else "Fail",
        "time": respTime if ok else -1
    })

    response.status_code == 200 if ok else 500
    return response


@app.get("/usage")
def checkUsage():
    size, status = utils.getUsage()
    ok = (status == True)
    response = jsonify({
        "status": "Ok" if ok else "Fail",
        "time": size if ok else -1
    })

    response.status_code == 200 if ok else 500
    return response



@app.get("/list")
def log():
    pass


app.run(host="0.0.0.0", port=8000)
