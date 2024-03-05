from flask import Flask, request, redirect
from replit import db

app = Flask(__name__, static_url_path='/static')
# path to the static file that stores my images

db["david"] = {"password" : "Baldy1"}
db["katie"] = {"password" : "k8t"}

@app.route('/')
def index():
  page = """<html>
    <body>
      <a href="/signup">Sign up</a>
      <br>
      <a href="/login">Log in</a>
    </body
    </html>"""
  return page

@app.route('/signup', methods=["GET","POST"])
def signup():
  page="""<form method = "post" action="/process">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Password: <input type="password" name="password" required> </p>
    <button type="submit">Sign Up</button>
  </form>"""
  return page

@app.route('/process', methods=["GET","POST"])
def process():
  form = request.form
  if form["username"].lower() in db.keys():
    return """User already in database
    <a href="/">Home</a>"""
  else:
    db[form["username"].lower()] = {'password':form['password']}
    return redirect("/login")


@app.route('/login', methods=["GET","POST"])
def login():
  page="""<form method = "post" action="/processlogin">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Password: <input type="password" name="password" required> </p>
    <button type="submit">Login</button>
  </form>"""
  return page

@app.route('/processlogin', methods=["POST"])
def processlogin():
  form = request.form
  try:
    if db[request.form["username"]]   ["password"]== request.form["password"]:
      return redirect("/yup")
    else:
      return redirect("/nope")
  except:
    return redirect("/nope")

@app.route("/nope")
def nope():
  return """<img src="static/nerdy.gif" height="100">"""
@app.route("/yup")
def yup():
  return """<img src="static/yup.gif" height="100">"""


app.run(host='0.0.0.0', port=81)

