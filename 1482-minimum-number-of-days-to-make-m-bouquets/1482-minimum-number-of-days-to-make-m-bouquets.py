class Solution:
    def minDays(self, bloomDay, m, k):

        # Impossible to make enough bouquets
        if m * k > len(bloomDay):
            return -1

        def check(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans