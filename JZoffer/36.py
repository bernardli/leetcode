# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.head = None
        self.pre = None
        tail = self.dfs(root)
        self.head.left = tail
        tail.right = self.head
        return self.head
        
    def dfs(self, root):
        if root == None:
            return None
        
        left = self.dfs(root.left)

        if self.head == None:
            self.head = root
            self.pre = root
        else:
            self.pre.right = root
            root.left = self.pre
            self.pre = root
        
        right = self.dfs(root.right)

        if right != None:
            return right
        return root
        