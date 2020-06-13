'''
注意:
这个方法思路没错, 但是leetcode的输入似乎有点问题, 在python3下无法通过
但python2可以通过(当然要稍微改改语法)
'''

from typing import List
import heapq

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
这个实现在heappush时, 除了val和node本身之外, 在中间插入了一个i
这是因为python的heap排序实现时, 只进行<判断, 所以当元祖里的第一位
等大时, 就会对元祖的第二位进行比较, 如果只插入val和node, 那么第二位
就是一个不可比较的ListNode实例, 会报错, 所以这里要插入一个可比较的值,
是多少无所谓, 反正值相同的节点的前后关系无所谓, 但是这个值必须唯一
不然会接着比较第三位
'''
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        head = ListNode(0)
        point = head
        for i, node in enumerate(lists):
            if type(node) != ListNode:
                continue
            heapq.heappush(h, (node.val, i, node))
        while h:
            val, i, node = heapq.heappop(h)
            point.next = node
            point = node
            if node.next != None:
                heapq.heappush(h, (node.next.val, i, node.next))
        return head.next

    def run(self):
        a = ListNode(1)
        a.next = ListNode(4)
        a.next.next = ListNode(5)
        b = ListNode(1)
        b.next = ListNode(3)
        b.next.next = ListNode(4)
        c = ListNode(2)
        c.next = ListNode(6)
        foo = self.mergeKLists([a, b, c])
        test = []
        while foo != None:
            test.append(foo.val)
            foo = foo.next
        print(test)

bar = Solution()
bar.run()
