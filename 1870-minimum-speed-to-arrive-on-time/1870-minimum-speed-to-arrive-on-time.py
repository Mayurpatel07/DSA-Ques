class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math 
        def check(mid):
            tt = 0 
            for i in range(len(dist)-1) :
                tt = tt + math.ceil(dist[i]/mid)
            i = len(dist)-1 
            tt = tt+ dist[i]/mid
            if tt<=hour :
                return True 
            else :
                return False    
            
        left = 1 
        right = 10**7 
        time = -1
        while left<=right:
            mid = left +(right-left)//2 
            if check(mid):
                time = mid
                right = mid-1 
            else :
                left = mid+1 

        if hour <= len(dist) - 1:
            return -1 
        else :
            return time
                