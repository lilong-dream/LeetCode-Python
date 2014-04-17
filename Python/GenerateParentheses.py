# Problem:  http://oj.leetcode.com/problems/generate-parentheses/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/23917967
# 1988lilong@163.com

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        res = []
        self.generate(n, n, "", res)
        return res
    
    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)

if __name__ == "__main__":
    slt = Solution()
    print slt.generateParenthesis(3)