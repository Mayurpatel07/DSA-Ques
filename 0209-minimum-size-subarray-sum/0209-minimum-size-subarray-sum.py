class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        win_sum = 0
        left = 0 
        minl = float("inf")


        for right in range(len(nums)):
            win_sum = win_sum+nums[right] 

            while win_sum >= target :
                minl = min(minl,right-left+1)
                win_sum = win_sum-nums[left]
                left = left+1 
        if minl == float('inf'):
            return 0 
        else :
            return minl