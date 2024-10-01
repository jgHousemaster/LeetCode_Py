class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        return self.check_sum(root, targetSum - root.val)

    def check_sum(self, root, count):
        if not root.left and not root.right:
            # 到达叶子节点
            if count == 0:
                return True
            else:
                return False
        # DFS
        if root.left:
            # 因为触底反弹条件没有处理空节点，此处要提前检查
            if self.check_sum(root.left, count - root.left.val):
                # 回溯判断左子树是否有符合的
                return True
        if root.right:
            if self.check_sum(root.right, count - root.right.val):
                return True
        return False
