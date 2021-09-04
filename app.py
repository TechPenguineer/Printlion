from flask import *

app = Flask(__name__)

@app.route("/")
def LOADER():
    return render_template("LOADER.html", TITLE="PrintLion")