class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_ = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                idx = stack.pop()
                if stack :
                    w = i-stack[-1]-1
                else :
                    w = i
                h = heights[idx]
                new = h*w
                max_ = max(max_, new)
            stack.append(i)
        return max_