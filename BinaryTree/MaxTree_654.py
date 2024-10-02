# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        # 数组为空
        if len(nums) == 0:
            return None
        # 寻找最大值
        max_num = float('-inf')
        for i in range(len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i
        # 构建本层根节点
        root = TreeNode(max_num)
        if len(nums) == 1:
            return root
        # 切割
        left_nums = nums[:max_index]
        right_nums = nums[max_index + 1:]
        # 对切割出来的两个数组进行递归建树
        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)
        # 返回本层根节点
        return root
