# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Base case: if the root is None, return 0
        if root is None:
            return 0
        
        # Initialize the sum of left leaves to 0
        total_sum = 0
        
        # Check if the left child exists and if it's a leaf
        if root.left and not root.left.left and not root.left.right:
            total_sum += root.left.val  # Add the value of the left leaf node
        
        # Recursively check the left and right subtrees
        total_sum += self.sumOfLeftLeaves(root.left)
        total_sum += self.sumOfLeftLeaves(root.right)
        
        return total_sum
