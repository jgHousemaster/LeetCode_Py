class Solution(object):
    def partition(self, s):
        self.path = []
        self.result = []
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s, startIndex):
        if startIndex == len(s):
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s[startIndex: i + 1]):
                self.path.append(s[startIndex: i + 1])
                self.backtracking(s, i + 1)
                self.path.pop()

    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
        """
        :type s: str
        :rtype: List[List[str]]
        """
