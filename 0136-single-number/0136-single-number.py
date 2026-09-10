class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            result = 0 
            for i in nums:
                result = result^i 
            return result


                