class Solution(object):
    def permute(self, nums):
        path = []
        result = []
        self.backtracking(nums, path, result)
        return result

    def backtracking(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                self.backtracking(nums, path, result)
                path.pop()

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
