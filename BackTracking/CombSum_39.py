class Solution(object):
    def combinationSum(self, candidates, target):
        self.path = []
        self.result = []
        self.backtracking(candidates, target, 0, 0)
        return self.result

    def backtracking(self, candidates, target, sum, startIndex):
        if sum > target:
            return
        if sum == target:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(candidates)):
            self.path.append(candidates[i])
            self.backtracking(candidates, target, sum + candidates[i], i)
            self.path.pop()
        return
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
