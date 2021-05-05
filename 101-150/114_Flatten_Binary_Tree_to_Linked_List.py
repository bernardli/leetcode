# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recursion(root, None)
        

    def recursion(self, root, tail):
        if root == None:
            return None
        
        # left
        if root.right != None:
            newRight = self.recursion(root.left, root.right)
        else:
            newRight = self.recursion(root.left, tail)
        root.left = None
        # right
        self.recursion(root.right, tail)
        if newRight != None:
            root.right = newRight
        if root.right == None:
            root.right = tail
            

        return root