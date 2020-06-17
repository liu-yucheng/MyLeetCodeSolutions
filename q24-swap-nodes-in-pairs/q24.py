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
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        temp = head
        temp2 = head.next
        temp3 = head.next.next
        temp2.next = temp
        temp.next = temp3
        head = temp2
        prev = temp
        curr = temp3
        while curr is not None and curr.next is not None:
            temp = curr
            temp2 = curr.next
            temp3 = curr.next.next
            temp2.next = temp
            temp.next = temp3
            prev.next = temp2
            prev = temp
            curr = temp3
        return head
