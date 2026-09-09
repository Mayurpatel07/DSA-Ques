class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0 
        res = False 
        for i in range(len(nums)):
            if nums[i] > nums[(i+1 )% len(nums) ]:
                count +=1 
        if count <= 1 :
            res = True 
        else :
            res = False 
        return res       