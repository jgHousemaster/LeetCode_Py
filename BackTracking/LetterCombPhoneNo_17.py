class Solution(object):
    def letterCombinations(self, digits):
        self.letter_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.result = []
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0, "")
        return self.result

    def backtracking(self, digits, index, path):
        if index == len(digits):
            self.result.append(path[:])
            return
        letters = self.letter_map[int(digits[index])]
        for c in letters:
            self.backtracking(digits, index + 1, path + c)
        return
        """
        :type digits: str
        :rtype: List[str]
        """
