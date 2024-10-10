# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- 这个题如果用迭代法，会有非常多需要处理的条件（父节点是否为空，每个 if 都得处理一遍）
- 在节点左右都有孩子时，将左子树的最右节点直接替换要删除的节点会更平衡，但操作复杂。
"""


class Solution(object):
    def deleteNode(self, root, key):
        # 没找到
        if root is None:
            return None
        # 找到了
        if root.val == key:
            # 这是个叶子节点，直接断掉这个节点和上面的连接
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                # 左边为空，把右边接给父节点
                return root.right
            elif root.right is None:
                # 右空，同理
                return root.left
            else:
                # 左右都有孩子，把左子树直接接到右边的最左
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        # 寻找目标值
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
