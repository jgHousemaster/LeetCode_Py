# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        # 如果一个节点为空，就直接返回另一个节点。都为空时也不过返回了空。节点下面的子树也都一并带上了。
        if not root1:
            return root2
        if not root2:
            return root1
        # 能到这说明两个节点都不空
        # 直接在 root1 上操作，节省空间
        root1.val += root2.val
        # 递归操作左右孩子
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        # 返回本层节点
        return root1
