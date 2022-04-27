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
        limits = {
            "recursive": 30,
            "memoized": 900,
            "array": 100000,
            "loop": 2000000,
            "matrix": 10000000
        }
        if n > limits[alg]:
            result["err"] = "This calculation consumes too much resources for such a large input. Please choose a more advanced algorithm. If you want to do the calculation for n greater than 10 million or experiment with the running time of the different methods, please clone the repository from <a href='https://github.com/IF-83/Fibonacci' target='_blank'>here</a> and run the program on your own computer."
            result["n"] = n
            return jsonify(result)
        start_time = time.time()
        f = str(methods[alg](n))
        end_time = time.time()
        result["n"] = n
        result["digits"] = len(f)
        result["fib"] = f
        result["sec"] = round(end_time -  start_time, 6)
        result["float_rep"] = f"{f[0]}.{f[1:16]}e+{len(f)-1}" if len(f) >= 20 else f
    except RecursionError as re:
        result["err"] = f"Parameter n = {n} is too large. Please try a non-recursive algorithm."
    except ValueError as ve:
        result["err"] = "Invalid input. Please type a positive integer for n and try again."
    except:
        result["err"] = "Unexpected error occurred. Please make sure to provide valid parameters and try again."
    return jsonify(result)


if __name__ == "__main__":
    app.run()
