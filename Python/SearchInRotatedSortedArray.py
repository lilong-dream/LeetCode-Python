# Problem:  http://oj.leetcode.com/problems/search-in-rotated-sorted-array/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/22864861
# 1988lilong@163.com

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        
        while left <= right:
            mid = (left + right) / 2
            
            if A[mid] == target:
                return mid
            
            if A[mid] >= A[left]:
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
    
if __name__ == "__main__":
    A = [4, 5, 6, 1, 2]
    
    slt = Solution()
    print slt.search(A, 5)
    print slt.search(A, 3)