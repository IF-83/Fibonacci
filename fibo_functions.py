

def fibo_recursive(n: int) -> int:
    """ naive recursion O(c^n) complexity (where c ~ 1.6) """
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)


def __fibos_recursion(n: int) -> int:
    """ auxiliary function """
    if n <= 0:
        raise Exception("Invalid argument: " + n)
    if n == 1:
        return [0,1]
    prev_fib = __fibos_recursion(n-1)
    return [prev_fib[1], sum(prev_fib)]


def fibo_recursive_linear(n: int) -> int:
    """ number of recursive calls is O(n); overall complexity: O(n^2) """
    if n == 0:
        return 0
    return __fibos_recursion[1]

