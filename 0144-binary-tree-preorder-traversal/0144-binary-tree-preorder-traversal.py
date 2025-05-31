# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        stk = [root]
        lst = []
        while stk:
            root = stk.pop()
            lst.append(root.val)
            if root.right:
                stk.append(root.right)
            if root.left:
                stk.append(root.left)
        return lst

    '''
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) 
        '''