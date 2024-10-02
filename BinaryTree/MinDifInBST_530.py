# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        self.result = float('inf')
        self.pre_node = None
        self.traverse(root)
        return self.result

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if self.pre_node:
            self.result = min(self.result, abs(root.val - self.pre_node.val))
        self.pre_node = root
        self.traverse(root.right)
