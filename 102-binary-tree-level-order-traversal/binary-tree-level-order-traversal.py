# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []  # This will store the result as a list of lists
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            current_level = []  # List to store nodes at the current level

            for _ in range(level_size):
                node = queue.popleft()  # Remove the node from the front of the queue
                current_level.append(node.val)  # Add the node's value to the current level list

                # Add the left and right children of the node to the queue (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)  # Add the current level to the result

        return result
