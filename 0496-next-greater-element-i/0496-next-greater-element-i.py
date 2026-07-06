class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dis={}

        for i in nums2:
            while stack and stack[-1]<i:
                popped = stack.pop()
                dis[popped] = i 

            stack.append(i)

        while stack :
            dis[stack.pop()] = -1 

        ans = [] 
        for i in nums1:
            ans.append(dis[i])
        return ans    