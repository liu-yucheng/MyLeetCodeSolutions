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
    def partition(self, head: ListNode, x: int) -> ListNode:
        less, notLess = None, None
        curr = head
        currLess, currNotLess = None, None
        while curr is not None:
            if curr.val < x:
                if less is None:
                    less = ListNode(curr.val)
                    currLess = less
                else:
                    currLess.next = ListNode(curr.val)
                    currLess = currLess.next
            else:
                if notLess is None:
                    notLess = ListNode(curr.val)
                    currNotLess = notLess
                else:
                    currNotLess.next = ListNode(curr.val)
                    currNotLess = currNotLess.next
            curr = curr.next
        if less is None:
            return notLess
        result = less
        currLess.next = notLess
        return result
