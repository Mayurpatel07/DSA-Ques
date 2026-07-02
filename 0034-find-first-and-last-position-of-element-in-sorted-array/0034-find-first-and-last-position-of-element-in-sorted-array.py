class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = 0 
        right = len(nums)

        while left < right :   #lower bound
            mid = left+(right-left)//2
            if nums[mid]>=target :
                right = mid 
            else :
                left = mid +1
        ans = left
        if ans == len(nums) or nums[ans] != target:  # check that is target exist or not 
            return[-1,-1] 
        else :
            left = 0    # upper bound 
            right = len(nums)
            while left < right :
                mid = left+(right-left)//2
                if nums[mid]>target :
                    right = mid 
                else :
                    left = mid +1
            return[ans,left-1]