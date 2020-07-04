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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None:
            return None
        if m == n:
            return head
        idx = 1
        curr = head
        nodes = []
        while curr is not None:
            if idx >= m and idx <= n:
                nodes.append(curr)
            if idx > n:
                break
            idx += 1
            curr = curr.next
        front = 0
        end = len(nodes) - 1
        while front < end:
            temp = nodes[end].val
            nodes[end].val = nodes[front].val
            nodes[front].val = temp
            front += 1
            end -= 1
        return head
