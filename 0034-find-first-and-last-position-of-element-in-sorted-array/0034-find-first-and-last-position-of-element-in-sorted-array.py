class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        found = False 
        while left<=right :
            mid = left+(right-left)//2
            if nums[mid]==target:
                found = True
                break
            elif nums[mid]<target:
                left = mid+1 
            else :
                right = mid-1

        if found == True:
            while left < right :
                mid = left+(right-left)//2
                if nums[mid]>=target :
                    right = mid 
                else :
                    left = mid +1
            ans = left
            left = 0 
            right = len(nums)
            while left < right :
                mid = left+(right-left)//2
                if nums[mid]>target :
                    right = mid 
                else :
                    left = mid +1
            return[ans,left-1]

        else :
            return[-1,-1]