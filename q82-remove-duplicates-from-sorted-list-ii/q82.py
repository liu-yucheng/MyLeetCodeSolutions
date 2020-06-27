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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        prev, curr, next = None, head, head.next
        removing = None
        while curr is not None:
            if removing is None:
                if next is None:
                    break
                if curr.val == next.val:
                    removing = curr.val
                    if prev is None:
                        head = next.next
                    else:
                        prev.next = next.next
                    curr = next.next
                    if curr is not None:
                        next = curr.next
                    else:
                        next = None
                else:
                    prev = curr
                    curr = next
                    if curr is not None:
                        next = curr.next
                    else:
                        next = None
            else:
                if removing == curr.val:
                    if prev is None:
                        head = next
                    else:
                        prev.next = next
                    curr = next
                    if curr is not None:
                        next = curr.next
                    else:
                        next = None
                elif next is not None and curr.val == next.val:
                    removing = curr.val
                    if prev is None:
                        head = next.next
                    else:
                        prev.next = next.next
                    curr = next.next
                    if curr is not None:
                        next = curr.next
                    else:
                        next = None
                else:
                    removing = None
                    prev = curr
                    curr = next
                    if curr is not None:
                        next = curr.next
                    else:
                        next = None
        return head
