# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        # 递归，如果数组为空则返回 None
        if len(inorder) == 0:
            return None
        # 建立本层递归的 root 节点，值为后序遍历的最后一位
        root = TreeNode(postorder[-1])
        # 减少不必要的操作
        if len(inorder) == 1:
            return root
        # 用 root 的值切割前序遍历
        root_index = inorder.index(root.val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        # 用左子树的长度切割后序遍历
        left_len = len(left_inorder)
        left_postorder = postorder[:left_len]
        right_postorder = postorder[left_len:-1]
        # 递归为左右子树分别进行建树操作，将子树的根节点收集作为本层根节点的左右孩子
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        # 返回本层根节点
        return root
