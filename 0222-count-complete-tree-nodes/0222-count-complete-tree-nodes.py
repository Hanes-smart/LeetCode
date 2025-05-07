# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    '''
        def lnode(node): # not a class method
            if not node: return 0
            return 1 + lnode(node.left)

        def rnode(node):
            if not node: return 0
            return 1 + rnode(node.right)

        l,r = lnode(root), rnode(root)
        
        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            (2**l) -1 #height of the prefect tree
            '''
       


      


        