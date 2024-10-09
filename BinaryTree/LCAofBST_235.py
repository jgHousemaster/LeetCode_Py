# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 如果 p 在当前节点左边，q 在当前节点右边，那么当前节点就是最近公共祖先（此处是分叉点，走向左右任意一边都会错过一个目标值）

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        l = min(p.val, q.val)
        r = max(p.val, q.val)
        while root:
            if root.val >= l and root.val <= r:
                return root
            elif root.val < l:
                root = root.right
            else:
                root = root.left