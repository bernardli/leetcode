# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        start = 0
        end = 0
        record = []
        index = 0

        p = head
        while p != None:
            record.append(p.val)
            p = p.next
            index += 1

        end = index - 1
        root = self.buildTree(record, start, end)

        return root

    def buildTree(self, record, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(val=record[start])
        center = (start + end) // 2
        leftRoot = self.buildTree(record, start, center - 1)
        rightRoot = self.buildTree(record, center + 1, end)

        return TreeNode(val=record[center], left=leftRoot, right=rightRoot)
