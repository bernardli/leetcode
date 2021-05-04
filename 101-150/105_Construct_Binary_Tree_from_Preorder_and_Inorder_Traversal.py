from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = self.recursion(preorder, 0, inorder, 0, len(inorder) - 1)
        return root

    def recursion(self, preorder, preIndex, inorder, start, end):
        if start > end:
            return None
        rootVal = preorder[preIndex]
        if start == end:
            return TreeNode(rootVal)
        rootIndex = start
        while inorder[rootIndex] != rootVal:
            rootIndex += 1
        leftRoot = self.recursion(preorder, preIndex+1, inorder, start, rootIndex - 1)
        rightRoot = self.recursion(preorder, preIndex + (rootIndex - start) + 1,inorder, rootIndex + 1, end)

        root = TreeNode(rootVal, leftRoot, rightRoot)
        return root
        
    def run(self):
        self.buildTree([3,9,20,15,7], [9,3,15,20,7])

foo = Solution()
foo.run()