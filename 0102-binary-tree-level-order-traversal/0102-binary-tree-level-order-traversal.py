# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []

        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)         # Store the node, not the value
                   
                if root.right:
                    next_queue.append(root.right)        # Same here
        
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
                
        return result


        