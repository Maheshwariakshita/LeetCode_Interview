# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        # Helper function to calculate the height of the tree
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the diameter with the maximum value of left_height + right_height
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        # Call the helper function on the root to initiate the recursion
        height(root)
        
        # Return the diameter found
        return self.diameter