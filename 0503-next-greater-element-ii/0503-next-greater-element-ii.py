class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans =[-1]*n
        for i in range(n*2):
            curr = i%n
            while stack and nums[stack[-1]]<nums[curr]:
                popped = stack.pop()
                ans[popped]=nums[curr]
            stack.append(curr)
        return ans