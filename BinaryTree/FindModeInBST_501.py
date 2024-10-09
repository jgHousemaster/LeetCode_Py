# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        self.pre_node = None
        self.count = 0
        self.max_count = 0
        self.result = list()
        self.traverse(root)
        return self.result

    def traverse(self, root):
        # 中序遍历，双指针
        if root is None:
            return
        self.traverse(root.left)
        # 计算当前数值的 count
        if self.pre_node is None or self.pre_node.val != root.val:
            self.count = 1
        else:
            self.count += 1
        # 根据 count 的情况处理 result 数组
        if self.count == self.max_count:
            self.result.append(root.val)
        elif self.count > self.max_count:
            # 当前 count 比之前的都大，则 result 数组作废，当前元素推入作为第一个结果
            self.max_count = self.count
            self.result = [root.val]
        self.pre_node = root
        self.traverse(root.right)
        return
        """
        :type root: TreeNode
        :rtype: List[int]
        """
