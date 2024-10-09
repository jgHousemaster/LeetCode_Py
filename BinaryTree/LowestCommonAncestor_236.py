# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 另一种解法：遇到 p 或者 q 就把节点直接传上来，如果左右子树都有返回值则返回本层节点。这种解法自动包含了 p 或者 q 本身就是公共祖先的情况。

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.result = None
        self.traverse(root, p, q)
        return self.result

    def traverse(self, root, p, q):
        if root is None:
            return False
        left_check = self.traverse(root.left, p, q)
        right_check = self.traverse(root.right, p, q)
        mid_check = (root == p or root == q)

        if (left_check and right_check) or ((left_check or right_check) and mid_check):
            self.result = root

        return left_check or right_check or mid_check