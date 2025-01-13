class Solution(object):
    def restoreIpAddresses(self, s):
        self.result = []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s, startIndex, pointCount):
        # 重点要搞清楚：startIndex 前面有点，i 后面有点
        if pointCount == 3:
            # 已经用尽分割点，验证最后的数字是否合法
            if self.is_valid(s[startIndex:]):
                self.result.append(s)
        for i in range(startIndex, min(len(s) - 1, startIndex + 3)):
            # startIndex 前面是上层回溯加的点儿或空，i 后面是这次循环打算放的点儿
            if self.is_valid(s[startIndex:i + 1]):
                s = s[:i + 1] + "." + s[i + 1:]
                self.backtracking(s, i + 2, pointCount + 1)
                # +2 是因为：1) 加了一个点儿；2) startIndex 前面有点儿，i 后面有点儿
                s = s[:i + 1] + s[i + 2:]

    def is_valid(self, s):
        # 判断字符串的子串是否是合法的 IP 段
        if len(s) == 0:
            # 空字符串
            return False

        num = int(s)
        if len(s) > 1 and s[0] == "0":
            # 前面有无意义的零
            return False
        elif num >= 0 and num <= 255:
            return True

        """
        :type s: str
        :rtype: List[str]
        """
