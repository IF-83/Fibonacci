import time
import fibo_functions
import fibo_classes

def main():
    print("Testing Fibonacci algorithms:")

    print("\nRecursive algorithm:")
    n = 35
    start_time = time.time()
    f = fibo_functions.fibo_recursive(n)
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")

    print("\nRecursive algorithm with memoization:")
    n = 996
    start_time = time.time()
    fibo_memoization = fibo_classes.Fibo_Memoization()
    f = fibo_memoization(n)
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")

    print("\nRecursive algorithm with one recursive call:")
    n = 996
    start_time = time.time()
    f = fibo_functions.fibo_recursive_linear(n)
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")

    print("\nTail-call optimizable recursive algorithm:")
    n = 900
    start_time = time.time()
    f = fibo_functions.fibo_tail_call(n)
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")

    print("\nSequential calculation and storing in array:")
    n = 250000
    start_time = time.time()
    f = fibo_functions.fibo_array(n)    
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")

    print("\nSequential calculation storing only the last 2 numbers:")
    n = 500000
    start_time = time.time()
    f = fibo_functions.fibo(n)
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")

    print("\nMatrix exponentiation with repeated squaring:")
    n = 3000000
    start_time = time.time()
    fibo_fastest = fibo_classes.Fibo_Fastest()
    f = fibo_fastest(n)
    end_time = time.time()
    print(f"For n = {n}: {format_very_big_numbers(f)} - Execution time: {round(end_time -  start_time, 6)} sec.")


def format_very_big_numbers(n: int) -> str:
    n = str(n)
    if len(n) <= 20:
        return n
    else:
        return f"{n[0]}.{n[1:16]}e+{len(n)-1}"


if __name__ == "__main__":
    main()
