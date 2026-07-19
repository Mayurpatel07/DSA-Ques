class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def fun(n):
            if n == 1 :
                return True 
            elif n <= 0 or n % 2 != 0:
                 return False 
            else :
                return fun(n//2)
        return fun(n)