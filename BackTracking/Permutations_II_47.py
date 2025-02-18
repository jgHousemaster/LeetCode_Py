class Solution(object):
    def permuteUnique(self, nums):
        # 对数组进行排序，这样一样的值会排在一块
        nums.sort()
        # 初始化
        path = []
        result = []
        used = [False] * len(nums)
        self.backtracking(nums, path, result, used)
        return result

    def backtracking(self, nums, path, result, used):
        if len(path) == len(nums):
            result.append(path[:])
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                # 树层去重：第 i 位与前一位相等且前一位这次未被选中（说明已经遍历过）
                # 这里也可以用 used[i - 1] == True，这样会只允许从后向前的那一次重复取数，但会做很多无用功
                continue
            if used[i] == True:
                # 该位已经在 path 里了
                continue
            # 收集该位
            path.append(nums[i])
            used[i] = True
            self.backtracking(nums, path, result, used)
            path.pop()
            used[i] = False
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
