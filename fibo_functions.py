

def fibo_recursive(n: int) -> int:
    """ naive recursion O(c^n) complexity (where c ~ 1.6) """
    if n <= 1:
        return n
    return fibo_recursive(n-1) + fibo_recursive(n-2)
