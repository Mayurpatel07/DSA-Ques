class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            ans = 0 
            D = 1
            for i in weights: 
                ans = ans +i 
                if ans > mid :
                    D = D +1 
                    ans = i 
            if D <= days :
                return True 
        left = max(weights)
        right = sum(weights)

        while left <=right :
            mid = left +(right-left)//2 
            if check(mid):
                capacity = mid
                right = mid-1 
            else :
                left = mid+1 
        return capacity

                