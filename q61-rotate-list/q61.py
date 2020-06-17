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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        if k == 0:
            return head
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        if length == 1:
            return head
        tarIdx = length - k % length
        tarIdx %= length
        if tarIdx == 0:
            return head
        newTail = head
        for _ in range(tarIdx - 1):
            newTail = newTail.next
        newHead = newTail.next
        oldTail = newHead
        while oldTail.next is not None:
            oldTail = oldTail.next
        newTail.next = None
        oldTail.next = head
        return newHead
