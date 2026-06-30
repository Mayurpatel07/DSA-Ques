class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid  
                break
            elif nums[mid]<target:
                ans = mid+1
                left = mid +1 
            else :
                right = mid-1 
        return left    