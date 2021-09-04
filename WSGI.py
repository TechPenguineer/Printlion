from flask import *

app = Flask(__name__)

@app.route("/")
def LOADER():
    return render_template("LOADER.html", TITLE="PrintLion")

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)