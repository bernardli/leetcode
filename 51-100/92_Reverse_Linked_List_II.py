# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_list(arr):
    if len(arr) == 0:
        return None
    head = ListNode(arr[0])
    p = head
    for i in range(1, len(arr)):
        p.next = ListNode(arr[i])
        p = p.next

    return head


def print_list(head):
    p = head
    arr = []
    while p != None:
        arr.append(p.val)
        p = p.next

    print(arr)


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        left = m
        rignt = n
        p = head
        i = 1
        pre_tail = None
        inter_head = None
        inter_tail = None
        while p != None:
            if i == left:
                inter_head = ListNode(p.val)
                inter_tail = inter_head
                while i < rignt:
                    p = p.next
                    i += 1

                    temp = inter_head
                    inter_head = ListNode(p.val)
                    inter_head.next = temp

                if pre_tail != None:
                    pre_tail.next = inter_head
                    inter_tail.next = p.next
                else:
                    head = inter_head
                    inter_tail.next = p.next

            pre_tail = p
            p = p.next
            i += 1

        return head

    def run(self):
        # print_list(self.reverseBetween(generate_list([1, 2, 3, 4, 5]), 2, 4))
        # print_list(self.reverseBetween(generate_list([5]), 1, 1))

        print_list(self.reverseBetween(generate_list([3, 5]), 1, 1))

foo = Solution()
foo.run()