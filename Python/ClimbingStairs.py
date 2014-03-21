# Problem:  http://oj.leetcode.com/problems/climbing-stairs/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/21650907
# 1988lilong@163.com

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a = []
        a.append(1)
        a.append(1)
        
        for i in range(2, n + 1):
            a.append(a[i - 1] + a[i - 2])
        
        return a[n]

if __name__ == "__main__":
    slt = Solution()
    result = slt.climbStairs(3)
    print result