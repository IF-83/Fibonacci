import time
import fibo_functions

def main():
    print("Testing Fibonacci algorithms:\n")

    print("Recursive algorithm:")
    n = 37
    current_time = time.time()
    print(f"For n = {n}: {fibo_functions.fibo_recursive(n)} - Execution time: {round(time.time() -  current_time, 3)} sec.")




if __name__ == "__main__":
    main()
