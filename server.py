from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate")
def calculate():
    print("Testing the endpoint.")
    r = {"x" : 10}
    return jsonify(r)


if __name__ == "__main__":
    app.run()
