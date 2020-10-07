from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None       # result link
        cur = None          # current node
        carry = False
        while l1 != None or l2 != None or carry:
            val = 0
            if l1 != None:
                val += l1.val
                l1 = l1.next
            if l2 != None:
                val += l2.val
                l2 = l2.next

            if carry:
                val += 1
                carry = False

            if val >= 10:
                carry = True
                val = val % 10

            if cur == None:
                result = ListNode(val)
                cur = result
            else:
                cur.next = ListNode(val)
                cur = cur.next
        return result

    def createLink(self, nums: List[int]):
        head = None
        cur = None
        for num in nums:
            if cur == None:
                head = ListNode(num)
                cur = head
            else:
                cur.next = ListNode(num)
                cur = cur.next
        return head

    def run(self):
        l1 = self.createLink([2, 4, 3])
        l2 = self.createLink([5, 6, 4])
        result = self.addTwoNumbers(l1, l2)
        while result != None:
            print(result.val)
            result = result.next


# test
foo = Solution()
foo.run()
