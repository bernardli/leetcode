# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = None
        count = 0
        prePoint = None
        newHead = None
        checkPoint = head
        
        if k == 1:
            return head

        p = head
        while p != None:
            count += 1

            if count == k:
                nextPoint = p.next
                subHead, subTail = self.reverse(checkPoint, p.next)
                subTail.next = nextPoint
                if prePoint != None:
                    prePoint.next = subHead
                else:
                    newHead = subHead
                prePoint = subTail
                checkPoint = subTail.next
                count = 0
                p = nextPoint
            else:
                p = p.next

        return newHead
    
    def reverse(self, checkPoint, nextPoint):
        subHead = None
        subTail = None
        p = checkPoint
        count = 1
        while p != nextPoint:
            temp = p
            p = p.next
            temp.next = subHead
            subHead = temp

            if count == 1:
                subTail = subHead
            count += 1

        return [subHead, subTail]