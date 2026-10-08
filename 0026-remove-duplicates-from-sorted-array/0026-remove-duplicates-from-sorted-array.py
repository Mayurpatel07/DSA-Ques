class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0 
        count = 1
        for fast in range(1,len(nums)):
            if nums[fast] != nums[slow]:
                slow = slow+1 
                nums[slow]=nums[fast]
                count = count+1 
        return slow+1


                





