from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def fromArray(cls, a):  # a: array
        if len(a) == 0:
            return None

        r = ListNode()  # result
        n = r  # node
        n.val = a[0]
        for e in a[1:]:  # e: element
            n.next = ListNode()
            n = n.next
            n.val = e
        return r

    def toArray(self):
        r = []  # result
        n = self  # node
        while n is not None:
            r.append(n.val)
            n = n.next
        return r

    def __str__(self):
        r = ""  # result
        n = self  # node
        while n is not None:
            r += str(n.val) + " -> "
            n = n.next
        return r


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        c = []  # cache
        node = head
        while node is not None:
            c.append(node)
            if len(c) > n + 1:
                c = c[1:]
            node = node.next
        next = None
        if len(c) >= 3:
            next = c[2]
        if len(c) == n + 1:
            c[0].next = next
        elif len(c) == n:
            newHead = None
            if len(c) >= 2:
                newHead = c[1]
            head = newHead
        return head
