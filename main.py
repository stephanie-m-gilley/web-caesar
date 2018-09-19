from flask import Flask, request
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<doctype html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/rotate" method="post">
            <label for ="rot">Rotate by:</label>
            <input type="text" name="rot" />
            <label for="textarea">Text:</label>
            <textarea></textarea>
            <input type="submit" value="Encrypt Text"/>
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/rotate", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + cgi.escape(first_name) + '</h1>'

app.run()