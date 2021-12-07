

class Fibo_Memoization:
    """ Recursion with memoization: O(n^2) time complexity, but O(n^2) space as well."""
    memory = [0,1]
    def __call__(self, n:int) -> int:
        if len(self.memory) >= n + 1:
            return self.memory[n]
        self.memory.append(self.memory[-1] + self.memory[-2])
        return self.__call__(n)
