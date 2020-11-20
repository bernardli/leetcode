# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        mainPointer = head
        lessHead = None
        lessPointer = None
        graterOrEqualHead = None
        graterOrEqualPointer = None

        while mainPointer != None:
            if mainPointer.val < x:
                if lessHead == None:
                    lessHead = mainPointer
                    lessPointer = lessHead
                else:
                    lessPointer.next = mainPointer
                    lessPointer = lessPointer.next
            else:
                if graterOrEqualHead == None:
                    graterOrEqualHead = mainPointer
                    graterOrEqualPointer = graterOrEqualHead
                else:
                    graterOrEqualPointer.next = mainPointer
                    graterOrEqualPointer = graterOrEqualPointer.next
            mainPointer = mainPointer.next

        if lessHead != None and graterOrEqualHead != None:
            lessPointer.next = graterOrEqualHead
            graterOrEqualPointer.next = None
            return lessHead
        elif lessHead != None and graterOrEqualHead == None:
            lessPointer.next = None
            return lessHead
        elif lessHead == None and graterOrEqualHead != None:
            graterOrEqualPointer.next = None
            return graterOrEqualHead
        else: # lessHead == None and graterOrEqualHead == None
            return head
