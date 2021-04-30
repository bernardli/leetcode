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


def test():
    head = generate_list([1, 2, 3, 4, 5])
    print_list(head)


if __name__ == '__main__':
    test()