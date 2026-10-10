class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        new = [0]*len(nums)
        p = 0 
        n = 1 
        for i in nums:
            if i >0 :
                new[p] = i 
                p +=2 
            else :
                new[n] = i
                n+=2 
        return new