from flask import Flask, request

app = Flask(__name__)

userDB = {
  "Torch":"MyNotGreatPassword",
  "David":"baldy1",
  "Nobody":"HowDidIGetHere?"
}

@app.route("/process", methods=["GET","POST"])
def process():
  page = ""
  form = request.form
  
  if form['username'] in userDB.keys():
    if form['password'] == userDB[form['username']]:
      page += f"Great {form['username']}"
    else:
      page += f"You've picked wrong {form['username']}"
  else:
    page += f"You've picked wrong {form['username']}"
  
  return page


@app.route('/')
def index():
  page = """<form method = "post" action="/process">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Password: <input type="password" name="password" required> </p>

    <button type="submit">Login</button>
  </form>
    """
  return page
  
app.run(host='0.0.0.0', port=81)
