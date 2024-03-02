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

  if form["madeOfMetal"] == "Yes":
    page += "Aha! A robot indeed"
  elif form["foodDropDown"] == "electrons":
    page += "No volts for you, robot!"
  else:
    page += "Welcome, fellow human"
    

  return page


@app.route('/')
def index():
  page = """<form method = "post" action="/process">
    <p>Are you made of metal?<br>
      <input type="radio" name="madeOfMetal" id="yes" value="Yes" required>
      <label for="yes">Yes</label><br>
      <input type="radio" name="madeOfMetal" id="no" value="No">
      <label for="no">No</label><br>
    </p>
    <p>What is infinity + 1?: <input type="text" name="question" required></p>
    <p>What is your favorite food?
      <select name="foodDropDown" id="food">
        <option value="brisket">Brisket</option>
        <option value="chili">Chili</option>
        <option value="electrons">Electrons</option>
      </select>
    </p>

    <button type="submit">Submit for Verification</button>
  </form>
    """
  return page

app.run(host='0.0.0.0', port=81)

