class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        p = head
        while p != None:
            oldNext = p.next
            p.next = Node(p.val, next=oldNext, random=None)
            p = p.next.next

        p = head
        q = head.next
        while p != None:
            if p.random == None:
                q.random = None
            else:
                q.random = p.random.next

            p = q.next
            if p != None:
                q = p.next

        newHead = head.next
        p = head
        q = newHead
        while p != None:
            p.next = q.next
            p = q.next
            if p != None:
                q.next = p.next
                q = q.next
            else:
                q.next = None


        return newHead

    def run(self):
        _7 = Node(7, None, None)
        _13 = Node(13, None, None)
        _11 = Node(11, None, None)
        _10 = Node(10, None, None)
        _1 = Node(1, None, None)

        head = _7
        _7.next = _13
        _7.random = None
        _13.next = _11
        _13.random = _7
        _11.next = _10
        _11.random = _1
        _10.next = _1
        _10.random = _11
        _1.next = None
        _1.random = _7

        self.copyRandomList(head)

foo = Solution()
foo.run()
    