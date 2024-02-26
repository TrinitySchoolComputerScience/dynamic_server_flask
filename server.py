from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
@app.route('/index')
def index():
    return """
           <html>
           <head>
             <link rel="stylesheet" href="styles.css">
           </head>
           <body>
             <h1>Welcome!</h1>
             <form action="/hello" method="GET">
               <label for="name">Enter your name:</label>
               <input type="text" name="name"><br><br>
               <input type="submit" value="Submit this ol' form">
             <form>
           </body>
           </html>
            """

@app.route('/hello')
def hello():
    #Getting information via the query string portion of a URL
    print(f"request.url={request.url}")
    print(f"request.url={request.query_string}")
    print(f"request.url={request.args.get('name')}")

    fruit = ["oranges", "apples", "blueberries"]
    response= f"""
           <html>
           <head>
           <link rel="stylesheet" href="styles.css">
           </head>
           <body>
           <h1>Hello, {request.args.get('name')}!</h1>

           What is your favorite fruit?</br>"""

    for f in fruit:
      response += f"<a href='fruit/{f}'>{f.capitalize()}</a></br>"""

    response+=f"""
               </body>
               </html>
                """
    return response


@app.route('/fruit/<fruit_name>')
def fruit_tips(fruit_name):
    #Getting information via the path portion of a URL
    food={
          "oranges": "https://en.wikipedia.org/wiki/Orange_(fruit)",
          "apples": "https://en.wikipedia.org/wiki/Apple",
          "blueberries": "https://en.wikipedia.org/wiki/Blueberry"
         }

    if fruit_name in food:
        tip = f"<a href='{food[fruit_name]}'>Check this out for more info on {fruit_name}!</a>"
    else:
        tip = "Hey! That fruit wasn't a legit choice!"

    response = f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <title>My Webpage</title>
                    <link rel="stylesheet" href="../styles.css">
                </head>
                <body>
                <h1>Fruit Tips</h1>
                {tip}
                </body>
                </html>"""

    return response

app.run(debug=True)
