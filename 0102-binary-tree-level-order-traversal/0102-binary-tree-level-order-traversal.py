# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        stack = deque([root])
        new = []
        
        if not root:
            return result
        result = [[root.val]]
        
        while stack:
            root = stack.popleft()
            if root.left:
                stack.append(root.left)         # Store the node, not the value
                new.append(root.left.val)       # Store the value for result
            if root.right:
                stack.append(root.right)        # Same here
                new.append(root.right.val)
            if new:
                result.append(new)
                new = []
                
        return result


        