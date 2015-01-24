# Problem:  http://oj.leetcode.com/problems/valid-parentheses/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/21694751
# 1988lilong@163.com

class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) == 0:
            return True
        
        st = [s[0]]
        
        i = 1
        while i < len(s):
            if len(st) == 0:
                st.append(s[i])
            else:
                tmp = st.pop()
                if self.isMatch(tmp, s[i]):
                    pass 
                else:
                    st.append(tmp)
                    st.append(s[i])
            
            i += 1
        
        if len(st) == 0:
            return True
        
        return False
            
    def isMatch(self, s, p):
        if (s == '(' and p == ')') or \
           (s == '{' and p == '}') or \
           (s == '[' and p == ']'):
            return True
        
        return False
    
if __name__ == "__main__":
    slt = Solution()
    s = "()"
    print slt.isValid(s)
