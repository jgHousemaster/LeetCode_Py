class Solution(object):
    def combine(self, n, k):
        # 回溯算法
        # 目前收集的集合路径
        self.path = []
        # 最终结果
        self.result = []
        self.backtracking(n, k, 1)
        return self.result

    def backtracking(self, n, k, start_index):
        # 终止条件，结果收集（集合大小已符合要求）
        if len(self.path) == k:
            # 浅拷贝 shallow copy，否则到最后回溯会把所有 path 变成 []
            self.result.append(self.path[:])
            return
        # 从宽度上遍历，剪枝
        for i in range(start_index, n - (k - len(self.path)) + 2):
            self.path.append(i)
            # start_index 从下一位开始
            self.backtracking(n, k, i + 1)
            self.path.pop()
        return
