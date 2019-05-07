#!/usr/bin/env python3

from flask import Flask, render_template, request, Response
from bson.json_util import dumps
import requests
import json

app = Flask(__name__)
API_ENDPOINT = "http://endpoint:5000/post"

@app.route("/")
def index():

        return render_template("index.html")


@app.route('/postendpoint', methods=['POST'])
def hello():
    nome = request.form['nomeform']
    email = request.form['emailform']
    data = '{"name": "%s", "email": "%s"}'% (nome, email)
    data1 = json.loads(data)
    headers = {'Content-type': 'application/json'}


    r = requests.post(API_ENDPOINT, data=json.dumps(data1), headers=headers)
    resultado = r.text

    response = {"message": "Usuário '%s' criado com sucesso!"%(nome)}
    return Response(dumps(response), status=201, content_type="application/json")

if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')

