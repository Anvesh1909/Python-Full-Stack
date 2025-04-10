# Flask
- flask is a python based library 
- the main objective of flask is to develop the end to end web application development
- we can install the flask library using `pip install flask`
```python

from flask import Flask

app = Flask(__name__)


@app.route("/1")
def home1():
    return "welcome to flask library for web application development"


@app.route("/2")
def home2():
    return "<h1>welcome to flask library for web application development</h1>"


if __name__ == "__main__":
    app.run(debug=True)
```

- how to add frontend in flask
- use templates folder to add all html pages 

```python
from flask import render_template

@app.route("/renderTemplate")
def renderTemplate():
    return render_template("renderTemplate.html")
```
- we can create a static folder inside the flask application 

- develop a flask application 
    - using templates to create a complete static application 

---
## how to implement satic folder in flask
- static 
    - images
    - css
    - js

- develop a flask application using complete frontend develop one complete dynamic webapplication using flask with html css and javascript
-  
