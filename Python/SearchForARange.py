# Problem:  http://oj.leetcode.com/problems/search-for-a-range/ 
# Analysis: http://blog.csdn.net/lilong_dream/article/details/22893675
# 1988lilong@163.com

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left = 0
        right = len(A) - 1
        
        result = [-1, -1]
        
        while left <= right:
            mid = (left + right) / 2
            
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                result[0] = mid
                result[1] = mid
                
                i = mid - 1
                while i >= 0 and A[i] == target:
                    result[0] = i
                    i -= 1
                
                i = mid + 1
                while i < len(A) and A[i] == target:
                    result[1] = i
                    i += 1
                    
                break
                
        return result

if __name__ == "__main__":
    A = [1, 2, 2, 4]
    
    slt = Solution()
    print slt.searchRange(A, 2)
            