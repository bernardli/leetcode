from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        p = head
        totalLen = 0
        while True:
            if p == None:
                break
            totalLen += 1
            p = p.next
        if totalLen == 0:
            return head
        rotateLen = k % totalLen
        if rotateLen == 0:
            return head
        i = 1
        newHead = None
        oldTail = None
        p = head
        while i <= totalLen:
            if i == totalLen - rotateLen:
                temp = p.next
                p.next = None
                p = temp
                i += 1
                continue
            elif i == totalLen - rotateLen + 1:
                newHead = p
                if newHead.next == None: # 最后一个节点
                    oldTail = newHead
            elif i == totalLen:
                oldTail = p
                break
            i += 1
            p = p.next

        oldTail.next = head
        return newHead

    def run(self):
        head = ListNode(0)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        print(self.rotateRight(head, 4))


foo = Solution()
foo.run()
