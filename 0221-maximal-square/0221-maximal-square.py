class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        max_side = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    if i == '0' and j == '0':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        )
                    max_side = max(max_side, dp[i][j])                    
        return max_side * max_side