# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 不用管题目说什么调整结构，二叉搜索树肯定能找到叶子位置插入。

class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            return TreeNode(val)
        result = root
        while root:
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return result
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                    return result
                else:
                    root = root.right

        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
