# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = root.val  # 题目说至少要有一个节点
        self.recursion(root)
        return self.result

    def recursion(self, root):
        if root == None:
            return 0

        leftMax = self.recursion(root.left)
        rightMax = self.recursion(root.right)
        self.result = max([self.result, leftMax + root.val + rightMax, root.val + leftMax, root.val + rightMax, root.val])
        return max([root.val, root.val + leftMax, root.val + rightMax])
