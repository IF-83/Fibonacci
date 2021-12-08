

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
    return __fibos_recursion(n)[1]


def __fibos_recursive_tail_call(l: list) -> list:
    """ auxiliary function """
    if l[0] == 0:
        return l
    return __fibos_recursive_tail_call([l[0]-1, l[2], l[1] + l[2]])


def fibo_tail_call(n: int) -> int:
    """ Time complexity is still O(n^2), but only O(n) space if optimized."""
    return __fibos_recursive_tail_call([n, 0, 1])[1]


def fibo_array(n: int) -> int:
    """ Time and space complexity: O(n^2)."""
    fibos = [0,1]
    if n >= 2:
        for i in range(2, n + 1):
            fibos.append(fibos[i-1] + fibos[i-2])
    return fibos[n]
