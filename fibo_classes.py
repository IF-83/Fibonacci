

class Fibo_Memoization:
    """ Recursion with memoization: O(n^2) time complexity, but O(n^2) space as well."""
    memory = [0,1]
    def __call__(self, n:int) -> int:
        if len(self.memory) >= n + 1:
            return self.memory[n]
        self.memory.append(self.memory[-1] + self.memory[-2])
        return self.__call__(n)


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
    
    