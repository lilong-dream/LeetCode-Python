# Problem:  http://oj.leetcode.com/problems/implement-strstr/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/23655843
# 1988lilong@163.com

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if not needle:
            return haystack
        
        len1 = len(haystack)
        len2 = len(needle)
        if len1 < len2:
            return None
        
        for i in range(len1 - len2 + 1):
            j = 0
            k = i
            while j < len2 and needle[j] == haystack[k]:
                j += 1
                k += 1
            
            if j == len2:
                return haystack[i:]
        
        return None

if __name__ == "__main__":
    slt = Solution()
    print slt.strStr("Hello", "ll")