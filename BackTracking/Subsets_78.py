class Solution(object):
    def subsets(self, nums):
        self.result = []
        self.path = []
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, startIndex):
        # 不论如何先收集当前 path
        self.result.append(self.path[:])
        # 不需要终止条件，因为 startIndex == len(nums) 的时候，for 循环就已经不会执行了
        # 回溯树横向遍历
        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

