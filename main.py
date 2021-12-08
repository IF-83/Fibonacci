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
    print(f"For n = {n}: {f} - Execution time: {round(end_time -  start_time, 3)} sec.")

    print("\nRecursive algorithm with memoization:")
    n = 996
    start_time = time.time()
    fibo_memoization = fibo_classes.Fibo_Memoization()
    f = fibo_memoization(n)
    end_time = time.time()
    if n > 100:
        f = float(f)
    print(f"For n = {n}: {f} - Execution time: {round(end_time -  start_time, 3)} sec.")

    print("\nRecursive algorithm with one recursive call:")
    n = 996
    start_time = time.time()
    f = fibo_functions.fibo_recursive_linear(n)
    end_time = time.time()
    if n > 100:
        f = float(f)
    print(f"For n = {n}: {f} - Execution time: {round(end_time -  start_time, 3)} sec.")



if __name__ == "__main__":
    main()
