# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.taversal(nums, 0, len(nums) - 1)

    def traversal(self, nums, left, right):
        # 在 [left, right] 区间里构造 BST
        if left > right:
            return None
        mid = (left + right) / 2
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid - 1)
        root.right = self.traversal(nums, mid + 1, right)
        return root
