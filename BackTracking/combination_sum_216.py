class Solution(object):
    def combinationSum3(self, k, n):
        # 初始化
        self.path = []
        self.result = []
        # 调用回溯函数
        self.back_tracking(k, n, 1, 0)
        return self.result

    def back_tracking(self, k, n, startIndex, sum):
        # 剪枝
        if sum > n:
            return
        # 终止条件
        if len(self.path) == k:
            if sum == n:
                self.result.append(self.path[:])
        # 横向遍历
        for i in range(startIndex, 9 - (k - len(self.path)) + 2):
            self.path.append(i)
            self.back_tracking(k, n, i + 1, sum + i)
            self.path.pop()
        return
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
