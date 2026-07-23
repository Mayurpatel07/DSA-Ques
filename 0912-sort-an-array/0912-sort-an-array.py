class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):

            result = []

            i = 0
            j = 0

            # Compare both arrays
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1

                else:
                    result.append(right[j])
                    j += 1

            # Copy remaining elements
            result.extend(left[i:])
            result.extend(right[j:])

            return result


        def merge_sort(arr):

            # Base Case
            if len(arr) <= 1:
                return arr

            # Divide
            mid = len(arr) // 2

            left = arr[:mid]
            right = arr[mid:]

            # Recursively sort both halves
            left = merge_sort(left)
            right = merge_sort(right)

            # Merge the sorted halves
            return merge(left, right)

        return merge_sort(nums)
