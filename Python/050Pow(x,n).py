# Problem:  http://oj.leetcode.com/problems/powx-n/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/21701775
# 1988lilong@163.com

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1.0 / self.power(x, -n)
        else:
            return self.power(x, n)
    
    def power(self, x, n):
        if n == 0:
            return 1
        
        tmp = self.power(x, n / 2)
        
        if n & 0x01 == 1:
            return tmp * tmp * x
        else:
            return tmp * tmp
        
if __name__ == "__main__":
    slt = Solution()
    print slt.pow(5, -1)        
