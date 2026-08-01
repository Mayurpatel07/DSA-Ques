from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores the number as the key and its index as the value
        num_to_index = {} 
        
        for current_index, current_num in enumerate(nums):
            needed_num = target - current_num
            
            # Check if the complement already exists in our map
            if needed_num in num_to_index:
                return [num_to_index[needed_num], current_index]
            
            # Otherwise, save the current number and its index
            num_to_index[current_num] = current_index
            
        return []

                