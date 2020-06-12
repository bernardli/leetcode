# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        point_1 = head
        point_2 = None
        count = 0
        while point_1.next != None:
            count += 1
            if count == n:      # 让point2指向倒数第n个的前一个
                point_2 = head
            elif count > n:
                point_2 = point_2.next
            point_1 = point_1.next
        if point_2 == None:
            head = head.next
        else:
            point_2.next = point_2.next.next
        return head

    # 这个不方便写测试, 懒得写了
            
        