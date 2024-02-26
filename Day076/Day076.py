from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
  page = """<html>
    <body>
      <h1>Welcome!</h1>
      <ul>
        <li><a href = "/portfolio">Torch02's Portfolio</a></li>
        <li><a href = "/linktree">Torch02's Links</a></li>
      </ul>
    </body>
  </html>"""
  return page

@app.route('/portfolio') # Creates the path to the home page
def portfolio(): # Subroutine to create the home page
  page = """<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Torch02's Portfolio</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>Torch02's best (?) Replits</h1>
  <script src="script.js"></script>

  <p>
    While I feel like I've grown leaps & bounds in my python ability, it was tough to find things that I wanted to share, which I felt showed that off.
  </p>
  
  <ul>
    <li>
      <h2>Day 47 - Top Trumps</h2>
      <p class="description">I chose NFL quarterbacks and their Madden 24 ratings.</p>
      <a href="https://github.com/Torch02/Replit100DaysOfPython/tree/main/Day047"><img src=static\images\Day47-TopTrumps.png width="60%"></a>
    </li>
    <li>
      <h2>Day 51 - Save to Disk</h2>
      <p class="description">It felt odd to write the whole to-do list as a single string, but I guess that's just my inexperience with serialization.</p>
      <a href="https://github.com/Torch02/Replit100DaysOfPython/tree/main/Day051"><img src=static\images\Day51-Save2Disk.png width="60%"></a>
    </li>
    <li>
      <h2>Day 53 - Saving Inventory</h2>
      <p class="description">Error handling to get around the first run, load failure issue from the other day.</p>
      <a href="https://github.com/Torch02/Replit100DaysOfPython/tree/main/Day053"><img src=static\images\Day53-Inventory.png width="60%"></a>
    </li>
    <li>
      <h2>Day 63 - Palidrome Library</h2>
      <p class="description">Recursion is always fun, when you get to do it again!</p>
      <a href="https://github.com/Torch02/Replit100DaysOfPython/tree/main/Day063"><img src=static\images/Day63-PalLibrary.png width="60%"></a>
    </li>
    <li>
      <h2>Day 65 - Object Oriented Characters</h2>
      <p class="description">This is all bringing up memories from my undergrad Comp Sci days...</p>
      <a href="https://github.com/Torch02/Replit100DaysOfPython/tree/main/Day065"><img src=static\images/Day65-OOP.png width="60%"></a>
    </li>
  </ul>
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>
"""
  return page # returns the contents of the page variable

@app.route('/linktree') # Creates the path to the home page
def linktree(): # Subroutine to create the home page
  page = """<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>Torch02's Linktree</h1>
  <script src="script.js"></script>

  <center><img src=static\images\hotel_headshot.jpg width="50%"></center>

  <ul>
    <li>
      <h3><a href=https://linkedin.com/in/torch02>LinkedIn</a></h3>
    </li>
    <li>
      <h3><a href=https://twitter.com/Torch02>Twitter</a></h3>
    </li>
    <li>
      <h3><a href=https://github.com/Torch02>GitHub</a></h3>
    </li>
  </ul>
 <!--
  This script places a badge on your repl's full-browser view back to your repl's cover
  page. Try various colors for the theme: dark, light, red, orange, yellow, lime, green,
  teal, blue, blurple, magenta, pink!
  -->
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
</body>

</html>"""
  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)

