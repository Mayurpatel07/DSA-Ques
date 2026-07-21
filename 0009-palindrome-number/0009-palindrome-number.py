class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases: 
        # 1. Negative numbers cannot be palindromes (e.g., -121 becomes 121-)
        # 2. Numbers ending in 0 (and not 0 itself) cannot be palindromes
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
            
        reversed_half = 0
        # Reverse the second half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + (x % 10)
            x //= 10
            
        # If the length is even, x should equal reversed_half
        # If the length is odd, x should equal reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
