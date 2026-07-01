class Solution:
    def search(self, nums: List[int], target: int) -> int:
        Found = False
        left = 0 
        right = len(nums)-1 

        while left < right :
            mid = left+(right-left)//2
            if nums[mid]>nums[right] :
                left = mid +1 
            else :
                right = mid 
        pivot = right 

        left = 0 
        right = pivot-1

        while left<=right :
            mid = left+(right-left)//2 
            if nums[mid]==target:
                return mid
                Found = True
                break
            elif nums[mid]<target:
                left = mid+1 
            else :
                right = mid -1 

        left = pivot 
        right = len(nums)-1
        while left<=right :
            mid = left +(right-left)//2 
            if nums[mid]==target:
                return mid
                Found = True
                break
            elif nums[mid]<target:
                left = mid+1 
            else :
                right = mid -1

        if Found == False :
            return -1