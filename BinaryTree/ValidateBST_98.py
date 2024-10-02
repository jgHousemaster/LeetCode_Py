# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        # 双指针法
        self.pre_node = None
        return self.isValid(root)

    def isValid(self, root):
        # 递归，中序遍历
        if not root:
            return True
        left_valid = self.isValid(root.left)
        if self.pre_node and self.pre_node.val >= root.val:
            return False
        self.pre_node = root
        right_valid = self.isValid(root.right)
        return left_valid and right_valid

