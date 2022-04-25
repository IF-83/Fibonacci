from flask import Flask, render_template, jsonify, request
import fibo_functions
import fibo_classes
import time
import sys

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate")
def calculate():
    result = {"n": None, "sec":None, "fib":None, "float_rep": None, "digits":None, "err":None }
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
        start_time = time.time()
        f = str(methods[alg](n))
        end_time = time.time()
        result["n"] = n
        result["digits"] = len(f)
        result["fib"] = f
        result["sec"] = round(end_time -  start_time, 6)
        result["float_rep"] = f"{f[0]}.{f[1:16]}e+{len(f)-1}" if len(f) >= 20 else f
    except RecursionError as re:
        result["err"] = f"Parameter n = {n} is too large for this algorithm. The maximum number of recursive calls is {sys.getrecursionlimit}. Please try a non-recursive algorithm."
    except ValueError as ve:
        result["err"] = "Invalid input. Please type a positive integer for n and try again."
    except:
        result["err"] = "Unexpected error occurred. Please make sure to provide valid parameters and try again."
    return jsonify(result)


if __name__ == "__main__":
    app.run()
