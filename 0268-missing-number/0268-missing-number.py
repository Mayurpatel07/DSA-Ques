class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        tsum = 0
        sums = 0 
        for i in range(1,len(nums)+1):
            tsum +=i
        for i in range(len(nums)):
            sums += nums[i]
        missing_num = tsum-sums
        return missing_num    
