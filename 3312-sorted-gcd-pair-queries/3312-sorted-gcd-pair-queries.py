from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # divCnt[g] = count of numbers divisible by g
        divCnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                divCnt[g] += freq[multiple]

        # exact[g] = pairs having gcd exactly g
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            cnt = divCnt[g]
            pairs = cnt * (cnt - 1) // 2

            multiple = 2 * g
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += g

            exact[g] = pairs

        prefix = []
        values = []

        cur = 0
        for g in range(1, mx + 1):
            if exact[g]:
                cur += exact[g]
                prefix.append(cur)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans