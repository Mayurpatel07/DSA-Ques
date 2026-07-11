from typing import List
from bisect import bisect_right

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        arr = sorted((nums[i], i) for i in range(n))

        values = [x[0] for x in arr]
        nodes = [x[1] for x in arr]

        pos = [0] * n
        for i in range(n):
            pos[nodes[i]] = i

        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        far = [0] * n
        for i in range(n):
            far[i] = bisect_right(values, values[i] + maxDiff) - 1

        LOG = n.bit_length()

        up = [far]
        for _ in range(1, LOG):
            prev = up[-1]
            curr = [0] * n
            for i in range(n):
                curr[i] = prev[prev[i]]
            up.append(curr)

        ans = []

        for u, v in queries:
            l = pos[u]
            r = pos[v]

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            if l > r:
                l, r = r, l

            if l == r:
                ans.append(0)
                continue

            jumps = 0
            cur = l

            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < r:
                    cur = nxt
                    jumps += 1 << k

            ans.append(jumps + 1)

        return ans