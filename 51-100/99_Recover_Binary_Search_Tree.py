# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        self.pred = None
        self.point1 = None
        self.point2 = None
        self.recursion(root)
        if self.point1 != None and self.point2 != None:
            temp = self.point1.val
            self.point1.val = self.point2.val
            self.point2.val = temp
        return root

    def recursion(self, root):
        if root == None:
            return

        # left
        self.recursion(root.left)
        # root
        if self.pred != None and self.pred.val > root.val:
            if self.point1 == None:
                self.point1 = self.pred
                self.point2 = root
            else:
                self.point2 = root
        self.pred = root
        # right 
        self.recursion(root.right)
        

    def run(self):
        pass

    
            
        