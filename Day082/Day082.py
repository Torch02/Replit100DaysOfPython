from flask import Flask, request

app = Flask(__name__)

@app.route('/language', methods=["GET"])
def language():
  get = request.args
  if get == {}:
    return "No data found"
  if get["lang"] == "eng":
    return "Welcome to our webpage."
  elif get["lang"] == "fr":
    return "Bonjour! Bienvenue ici."

@app.route('/', methods=["GET"])
def index():
  return "No data"

app.run(host='0.0.0.0', port=81)
