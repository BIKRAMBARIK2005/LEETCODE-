class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        copy = [row[:] for row in board]
        directions =[
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),            (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for i in range(m):
            for j in range(n):
                live = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < m and 0 <= y < n:
                        if copy[x][y] == 1:
                            live += 1
                if copy[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 0
                else:
                    if live == 3:
                        board[i][j] = 1

        
        