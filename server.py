from flask import Flask, render_template, jsonify, request
import fibo_functions
import fibo_classes

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

        methods = {
            "recursive":fibo_functions.fibo_recursive,
            "memoized":fibo_classes.Fibo_Memoization(),
            "array":fibo_functions.fibo_array,
            "loop":fibo_functions.fibo,
            "matrix":fibo_classes.Fibo_Fastest()
        }

        f = methods[alg](n)
        result["fib"] = f

    except:
        result["err"] = "Invalid parameters."
    return jsonify(result)


if __name__ == "__main__":
    app.run()
