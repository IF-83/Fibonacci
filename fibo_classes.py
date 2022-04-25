import sys

class Fibo_Memoization:
    """ Recursion with memoization: O(n^2) time complexity, but O(n^2) space as well."""
    def __init__(self) -> None:
        self.memory = [0,1]

    def __call__(self, n:int) -> int:
        if len(self.memory) >= n + 1:
            return self.memory[n]
        self.memory.append(self.memory[-1] + self.memory[-2])
        return self.__call__(n)


class Fibo_Fastest:
    """If my calculations are correct the complexity is O(n*log^2(n)) and O(n) space."""
    def __call__(self, n):
        if n == 0:
            return 0
        # calculates the nth power of the following matrix by repeated squaring:
        #          | 0   1 |
        #          | 1   1 |   -> the bottom left element is the nth Fibonacci number.
        F = Mtx_2_times_2(0,1,1,1)
        F = F**n
        return F.b


class Mtx_2_times_2:
    a, b, c, d = 0, 0, 0, 0  #columnwise
    
    # |a, c|
    # |b, d|

    def __init__(self, a, b, c, d) -> None:
        self.a, self.b, self.c, self.d = a, b, c, d
        return 

    def __str__(self) -> str:
        na, nb, nc, nd = len(str(self.a)), len(str(self.b)), len(str(self.c)), len(str(self.d)) 
        nm = max([na,nb,nc,nd])
        return f"| {' '*(nm - na) + str(self.a)}, {' '*(nm - nc) + str(self.c)} |\n| {' '*(nm - nb) + str(self.b)}, {' '*(nm - nd) + str(self.d)} |" 
    
    def __mul__(self, other):
        return Mtx_2_times_2(self.a * other.a + self.c * other.b, 
                             self.b * other.a + self.d * other.b,  
                             self.a * other.c + self.c * other.d,
                             self.b * other.c + self.d * other.d)
    
    def __pow__(self, n):
        if n <= 0:
            raise Exception("Invalid argument: " + n)
        i = 0
        E = Mtx_2_times_2(1,0,0,1)
        while n > 0:
            if n % 2 == 1:
                E *= self
            self *= self
            n //= 2
            i += 1
        return E