from flask import Flask, jsonify, request
from enigma_gubs_ian.myfunctions import *

app = Flask("Enigmas API - Ian e Gubs")

@app.route("/para_one_hot", methods=["POST"])
def para_one_hot():
    data = request.json
    msg = data["msg"]
    one_hot = para_one_hot(msg)
    return jsonify({"one_hot": one_hot.tolist()}, 200)

@app.route("/para_string", methods=["POST"])
def para_string():
    data = request.json
    M = np.array(data["M"])
    string = para_string(M)
    return jsonify({"string": string}, 200)

@app.route("/cifrar", methods=["POST"])
def cifrar():
    data = request.json
    msg = data["msg"]
    encrypted = cifrar(msg, P)
    return jsonify({"encrypted": encrypted}, 200)

@app.route("/de_cifrar", methods=["POST"])
def de_cifrar():
    data = request.json
    msg = data["msg"]
    decrypted = de_cifrar(msg, P)
    return jsonify({"decrypted": decrypted}, 200)

@app.route("/enigma", methods=["POST"])
def enigma():
    data = request.json
    msg = data["msg"]
    encrypted = enigma(msg, P, E)
    return jsonify({"encrypted": encrypted}, 200)

@app.route("/de_enigma", methods=["POST"])
def de_enigma():
    data = request.json
    msg = data["msg"]
    decrypted = de_enigma(msg, P, E)
    return jsonify({"decrypted": decrypted}, 200)