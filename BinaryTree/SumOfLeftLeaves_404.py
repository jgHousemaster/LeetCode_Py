class Solution(object):
    def sumOfLeftLeaves(self, root):
        # 后序遍历
        if root is None:
            return 0
        leftSum = self.sumOfLeftLeaves(root.left)
        rightSum = self.sumOfLeftLeaves(root.right)

        total = leftSum + rightSum
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        return total
