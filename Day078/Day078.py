from flask import Flask

app = Flask(__name__, static_url_path='/static')

thoughts = {
  "77" : "I am tiring of this webdev stuff...",
  "78" : "To be honest when I was first reading the description of today's challenge, I thought I was about to be told to create a webpage with unsanitized input. The security guy in me freaked out a little."
}

@app.route('/<pageNumber>')
def index(pageNumber):

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page = page.replace("{dayNumber}",pageNumber)
  page = page.replace("{text}",thoughts[pageNumber])
  if pageNumber < 100:
    page = page.replace(f"main/Day{pageNumber}",f"main/Day0{pageNumber}")
  return page

app.run(host='0.0.0.0', port=81)

