# Problem:  http://oj.leetcode.com/problems/3sum/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/21645437
# 1988lilong@163.com

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()

        result = []
        
        i = 0
        while i < len(num) - 2:
            if i > 0 and num[i] == num[i - 1]:
                i += 1
                continue
            
            j = i + 1
            k = len(num) - 1
            
            while j < k:
                if num[i] + num[j] + num[k] > 0:
                    k -= 1
                elif num[i] + num[j] + num[k] < 0:
                    j += 1
                else:
                    tmp = [num[i], num[j], num[k]]
                    result.append(tmp)
                    
                    j += 1
                    k -= 1
                    
                    while j < k and num[j] == num[j - 1]:
                        j += 1
                    while j < k and num[k] == num[k + 1]:
                        k -= 1
            i += 1
                        
        return result 
      
if __name__ == "__main__":
    slt = Solution()
    num = [-1, 0, 1, 2, -1, -4]
    result = slt.threeSum(num)
    print result
