class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        # return nums       

        count0= 0
        count1= 0
        count2= 0 
        for c in range(len(nums)):
            if nums[c] ==0:
                count0 +=1 
            elif nums[c]==1:
                count1 +=1 
            else:
                count2 +=1
        i = 0 
        for _ in range(count0):
            nums[i]=0 
            i +=1 
        for _ in range(count1):
            nums[i]=1
            i+=1
        for _ in range(count2):
            nums[i]=2 
            i+=1 
        return nums
         
