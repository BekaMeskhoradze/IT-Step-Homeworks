from flask import Flask, render_template
from models import movies

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html/', movies=movies)

if __name__ == "__main__":
    app.run(debug=True)