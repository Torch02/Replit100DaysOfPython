from flask import Flask, redirect, request

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=["GET"])
def index():
  page = """<html>
    <head></head>
    <body>
      <h1>Welcome!</h1>
      <ul>
        <li><a href = "/portfolio">Torch02's Portfolio</a></li>
        <li><a href = "/linktree">Torch02's Links</a></li>
      </ul>
    </body>
  </html>"""
  get = request.args
  if get["theme"] == "blue":
    page.replace('<head></head>','<head><link href="/static/css/blue.css" rel="stylesheet" type="text/css" /></head>')
  elif get["theme"] == "green":
    page.replace('<head></head>','<head><link href="/static/css/green.css" rel="stylesheet" type="text/css" /></head>')
  return page

@app.route('/blogroot', methods=["GET"])
def blogroot():
  myName = "Torch02"
  title = "My blog's First entry"
  text = "This is an interesting functionality from Flask, but I didn't exactly decide to learn python in order to create webpages..."
  image = "hotel_headshot.jpg"
  link = "https://github.com/Torch02"

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page =  page.replace("{name}", myName)
  page =  page.replace("{title}", title)
  page =  page.replace("{text}", text)
  page =  page.replace("{image}", image)
  page =  page.replace("{link}", link)
  get = request.args
  if get != {}:
    page = page.replace("{style}",get["theme"])
  else:
    page =  page.replace("{style}","style")
  return page

@app.route('/blogend', methods=["GET"])
def blogend():
  myName = "Torch02"
  title = "My blog's Last entry"
  text = "I hope this is my last webpage..."
  image = "hotel_headshot.jpg"
  link = "https://github.com/Torch02"

  page = ""
  f = open("template/portfolio.html", "r")
  page = f.read()
  f.close()
  page =  page.replace("{name}", myName)
  page =  page.replace("{title}", title)
  page =  page.replace("{text}", text)
  page =  page.replace("{image}", image)
  page =  page.replace("{link}", link)
  get = request.args
  if get != {}:
    page = page.replace("{style}",get["theme"])
  else:
    page =  page.replace("{style}","style")
  return page

@app.route('/first')
def first():
  return redirect("/blogroot")

@app.route('/last')
def last():
  return redirect("/blogend")

app.run(host='0.0.0.0', port=81)

