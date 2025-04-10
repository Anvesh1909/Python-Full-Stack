from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def AllPages():
    r = '''
        <ol>
            <li>/1</li>
            <li>/2</li>
            <li>/renderTemplate</li>
            <li>/staticPage</li>
        </ol>
    '''
    return render_template('route.html')

@app.route("/1")
def home1():
    return "welcome to flask library for web application development"


@app.route("/2")
def home2():
    return "<h1>welcome to flask library for web application development</h1>"



@app.route("/renderTemplate")
def renderTemplate():
    return render_template("renderTemplate.html")


@app.route("/staticPage")
def staticPage():
    # return "static page"
    return render_template('staticPage.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')



if __name__ == "__main__":
    app.run(debug=True)