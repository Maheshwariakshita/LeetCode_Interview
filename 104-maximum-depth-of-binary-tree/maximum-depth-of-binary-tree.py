# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.right is None:
            return self.maxDepth(root.left)+1
        if root.left is None :
            return self.maxDepth(root.right)+1
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1






        # if root is None: 
        #     return 0 
        # else: 
        #     left_height = self.maxDepth(root.left) 
        #     right_height = self.maxDepth(root.right) 
        #     return max(left_height, right_height) + 1 