class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math 
        def check(mid):
            hours = 0 
            for i in piles:
                hours += math.ceil(i/mid)
            return hours<=h 

        # check()

        left = 1
        right = max(piles)
        while left<=right :
            mid = left+(right-left)//2 
            if check(mid) :
                ans = mid 
                right = mid -1 
            else :
                left = mid +1 
        return ans