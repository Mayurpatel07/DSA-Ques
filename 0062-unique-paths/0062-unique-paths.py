class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}

        def path(row, col):

            if row == m or col == n:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = path(row + 1, col) + path(row, col + 1)

            return memo[(row, col)]

        return path(0, 0)