class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = [] 
        nums.sort()
        for i in range(len(nums)-1):
            if i>0 and nums[i] == nums[i-1] :
                continue
            l = i+1 
            r = len(nums)-1
            while l<r :

                if nums[i]+nums[l]+nums[r] == 0 :
                    t = [nums[i],nums[l],nums[r]]
                
                    ans.append(t)
                    l +=1 
                    r -=1 
                    while l<r and nums[l]==nums[l-1]:
                        l+=1 
                    while l<r and nums[r]==nums[r+1]:
                        r-=1 
                elif nums[i]+nums[l]+nums[r] > 0 :
                    r-=1 
                else :
                    l +=1
        return ans