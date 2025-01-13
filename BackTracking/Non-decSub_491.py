class Solution(object):
    def findSubsequences(self, nums):
        path = []
        result = []
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        if len(path) > 1:
            result.append(path[:])
        for i in range(startIndex, len(nums)):
            if len(path) == 0 or nums[i] >= path[-1]:
                if i > startIndex and nums[i] in nums[startIndex:i]:
                    # 去重：就在这个 for 循环里已经取过该值，就不能再取了
                    continue
                path.append(nums[i])
                self.backtracking(nums, i + 1, path, result)
                path.pop()