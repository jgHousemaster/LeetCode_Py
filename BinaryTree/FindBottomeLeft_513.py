# self 直接在函数里初始化是为了 OJ 系统，在开发时应该在 init 里初始化。
from collections import deque


class Solution(object):
    def findBottomLeftValue(self, root):
        self.max_depth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, root, depth):
        if not root.left and not root.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = root.val
        if root.left:
            self.traversal(root.left, depth + 1)
        if root.right:
            self.traversal(root.right, depth + 1)

    @staticmethod
    def findBottomLeftValue_1(root):
        # 层序遍历，初始化
        depth = 0
        max_depth = float('-inf')
        result = None
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            depth += 1
            while size:
                cur_node = queue.popleft()
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                if depth > max_depth:
                    max_depth = depth
                    result = cur_node.val
                size -= 1

        return result