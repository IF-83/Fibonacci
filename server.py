from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate")
def calculate():
    result = {"n": None, "sec":None, "fib":None, "float_rep": None, "err":None }
    try:
        n = int(request.args.get("n"))
        alg = request.args.get("method")
        result["n"] = n**2
        result["err"] = alg
    except:
        result["err"] = "Invalid parameters."
    return jsonify(result)


if __name__ == "__main__":
    app.run()
