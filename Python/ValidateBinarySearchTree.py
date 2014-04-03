# Problem:  http://oj.leetcode.com/problems/validate-binary-search-tree/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/22780563
# 1988lilong@163.com

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTImpl(root, -2**31, 2**31 - 1)
    
    def isValidBSTImpl(self, root, min, max):
        if root == None:
            return True
        
        return root.val > min and root.val < max \
               and self.isValidBSTImpl(root.left, min, root.val) \
               and self.isValidBSTImpl(root.right, root.val, max)
                
if __name__ == "__main__":
    n1 = TreeNode(0)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    
    slt = Solution()
    print slt.isValidBST(n1)