# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 计数
        count = 0
        p = head
        while p != None:
            count += 1
            p = p.next
        if count == 1:
            return head

        # 分割
        mid = 0
        if count % 2 == 0:
            mid = count // 2
        else:
            mid = count // 2 + 1
        count = 0
        p = head
        line2 = None
        while p != None:
            count += 1
            if count == mid:
                line2 = p.next
                p.next = None
                break
            p = p.next

        
        # 转置
        q = None
        p = line2
        while p != None:
            temp = p.next
            p.next = q
            q = p
            p = temp

        # 拼合
        p = head
        # q = line2
        while p != None and q != None:
            temp = p.next
            p.next = q
            temp2 = q.next
            q.next = temp
            p = temp
            q = temp2

        return head