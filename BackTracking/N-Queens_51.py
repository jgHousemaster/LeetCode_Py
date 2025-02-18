class Solution(object):
    def solveNQueens(self, n):
        # 建立空棋盘
        chessboard = ['.' * n for _ in range(n)]
        # 结果
        result = []

        self.backtracking(chessboard, n, 0, result)
        return result

    def backtracking(self, chessboard, n, row, result):
        # 收集结果
        if row == n:
            result.append(chessboard[:])
        # 遍历每一列
        for col in range(n):
            if self.isValid(chessboard, n, row, col):
                # 这个位置可以落子，递归后面的行
                chessboard[row] = '.' * col + 'Q' + '.' * (n - col - 1)
                self.backtracking(chessboard, n, row + 1, result)
                chessboard[row] = '.' * n

    def isValid(self, chessboard, n, row, col):
        # 判断该位置是否可以落子
        # 竖向判断
        for i in range(row):
            if chessboard[i][col] == 'Q':
                return False
        # 斜向判断，只需判断该子以上的行
        for i in range(1, row + 1):
            # 向左
            if col - i >= 0 and chessboard[row - i][col - i] == 'Q':
                return False
            # 向右
            if col + i < n and chessboard[row - i][col + i] == 'Q':
                return False
        return True

        """
        :type n: int
        :rtype: List[List[str]]
        """
