class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        path = []
        result = []
        self.backtracking(nums, 0, path, result)
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

    def backtracking(self, nums, startIndex, path, result):
        # 收集结果
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i - 1]:
                # 去重
                continue
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()
