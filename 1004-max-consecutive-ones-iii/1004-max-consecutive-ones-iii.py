class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0 
        left = 0 
        max_arr = 0 
        for right in range(len(nums)):

            if nums[right] == 0 :
                count = count +1
            
            while count > k :
                if nums[left] == 0 :
                    count = count -1 
                left = left +1 

            max_arr = max(max_arr,right-left+1)
        return max_arr 