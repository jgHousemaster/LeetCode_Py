# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        self.sum = 0
        self.traversal(root)
        return root

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.right)
        root.val += self.sum
        self.sum = root.val
        self.traversal(root.left)
        return