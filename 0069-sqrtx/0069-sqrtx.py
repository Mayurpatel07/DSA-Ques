class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0 
        right = x
        ans = 0 

        while left <=right:
            mid = left+(right-left)//2
            sq = mid*mid
            if sq==x:
                ans = mid 
                break 
            elif sq>x :
                right = mid-1 
            else :
                ans = mid    
                left = mid+1
        return ans