class Solution:
    def fib(self, n: int) -> int:
        def fub(n):
            if n == 0 :
                return 0 
            elif n == 1 :
                return 1 
            else :
                return fub(n-1)+fub(n-2)
        return fub(n)

