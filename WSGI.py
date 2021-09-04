from flask import *

app = Flask(__name__)

@app.route("/")
def LOADER():
    return render_template("MAIN.html", TITLE="PrintLion")

if __name__ == "__main__":
    """export FLASK_RUN_PORT=8000"""
    app.run(host="localhost", port=8000, debug=True)