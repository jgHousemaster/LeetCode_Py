class Solution(object):
    # 使用 used 数组：如果前一位没被用过，说明不在 path 中，是要去掉的重复（树层重复）
    def combinationSum2(self, candidates, target):
        # 初始化
        self.result = []
        self.path = []
        self.used = [0] * len(candidates)
        # 对数组进行排序，方便去重
        candidates.sort()
        # 调用回溯函数
        self.backtracking(candidates, target, 0, 0)
        return self.result

    def backtracking(self, candidates, target, sum, startIndex):
        # 终止条件处理
        if sum > target:
            return
        if sum == target:
            self.result.append(self.path[:])
        for i in range(startIndex, len(candidates)):
            # 去重：如果该位与上一位一致，且上一位并没有出现在 path 中（unused），则跳过
            if i > 0 and candidates[i] == candidates[i - 1] and self.used[i - 1] == 0:
                continue
            self.path.append(candidates[i])
            self.used[i] = 1
            self.backtracking(candidates, target, sum + candidates[i], i + 1)
            self.used[i] = 0
            self.path.pop()
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

# 优化：不使用 used 数组，如果该位与上一位一致，且该位不是本层起点，则跳过

class Solution2(object):
    def combinationSum22(self, candidates, target):
        # 初始化
        self.result = []
        self.path = []
        # 对数组进行排序，方便去重
        candidates.sort()
        # 调用回溯函数
        self.backtracking(candidates, target, 0, 0)
        return self.result

    def backtracking2(self, candidates, target, sum, startIndex):
        # 终止条件处理
        if sum > target:
            return
        if sum == target:
            self.result.append(self.path[:])
        for i in range(startIndex, len(candidates)):
            # 去重：如果该位与上一位一致，且该位不是本层起点，则跳过
            if i > startIndex and candidates[i] == candidates[i - 1]:
                continue
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum + candidates[i], i + 1)
            self.path.pop()
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
