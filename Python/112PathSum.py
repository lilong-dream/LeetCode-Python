# Problem:  http://oj.leetcode.com/problems/path-sum/
# Analysis: http://blog.csdn.net/lilong_dream/article/details/22875143
# 1988lilong@163.com

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        
        if root.left == None and root.right == None:
            return root.val == sum
        
        return self.hasPathSum(root.left, sum - root.val) \
                or self.hasPathSum(root.right, sum - root.val)

if __name__ == "__main__":
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
    n1 = TreeNode(5)
    n2 = TreeNode(4)
    n3 = TreeNode(8)
    n4 = TreeNode(11)
    n5 = TreeNode(13)
    n6 = TreeNode(4)
    n7 = TreeNode(7)
    n8 = TreeNode(2)
    n9 = TreeNode(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.left = n5
    n3.right = n6
    n4.left = n7
    n4.right = n8
    n6.right = n9
    
    slt = Solution()
    print slt.hasPathSum(n1, 22)
