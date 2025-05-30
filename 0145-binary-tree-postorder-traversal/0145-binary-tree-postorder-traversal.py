# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stk = [root]
        lst = []
        while stk:
            root = stk.pop()
            lst.append(root.val)

            if root.left:
                stk.append(root.left)
            
            if root.right:
                stk.append(root.right)
        return lst[::-1]
       
'''
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
'''
        