class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)-1
        for i in range(n):
            for j in range(i,n):
                if nums[i]+nums[j+1]==target :
                    return i,j+1
                    break 
