class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0 
        count = 0 
        for i in range(len(nums)):
            if nums[i] == 1 :
                count = count +1 
                m = max(m,count)
            else :
                count = 0 
        return m 