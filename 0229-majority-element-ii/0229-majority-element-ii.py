class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        a = n/3 
        b = {}
        c = []
        for i in nums:
            if i in b :
                b[i] = b[i]+1
            else :
                b[i] = 1 
        for key,value in b.items():
            if value > a :
                c.append(key)  
        return c      