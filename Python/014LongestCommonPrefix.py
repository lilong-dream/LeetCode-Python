# Problem:  http://oj.leetcode.com/problems/longest-common-prefix/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/22886331
# 1988lilong@163.com

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    return (strs[0])[0 : i]
                
        return strs[0]
    
if __name__ == "__main__":
    strs = ["abc", "abcd", "ab"]
    
    slt = Solution()
    print slt.longestCommonPrefix(strs)
