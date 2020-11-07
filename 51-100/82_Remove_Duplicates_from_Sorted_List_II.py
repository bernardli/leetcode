# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        result = None
        newTail = None
        pointer = head.next

        # if pointer == None:
        #     return head

        priorNum = head.val
        priorNumCount = 1
        while pointer != None:
            if pointer.val == priorNum:
                priorNumCount += 1
                pointer = pointer.next
                continue

            # pointer.val != priorNum
            if priorNumCount <= 1:
                if result == None:
                    result = ListNode(priorNum)
                    newTail = result
                else:
                    newTail.next = ListNode(priorNum)
                    newTail = newTail.next

            priorNum = pointer.val
            priorNumCount = 1
            pointer = pointer.next

        if priorNumCount <= 1:
            if result == None:
                result = ListNode(priorNum)
                newTail = result
            else:
                newTail.next = ListNode(priorNum)
                newTail = newTail.next

        return result
            


    def run(self):
        pass

