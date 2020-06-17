class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        d = self  # digit
        r = "linked list: "  # result
        while d is not None:
            r += str(d.val) + " -> "
            d = d.next
        return r


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        d1 = l1  # digit 1
        d2 = l2  # digit 2
        r = ListNode()  # result
        rd = r  # result digit
        c = 0  # carry
        fd = True  # first digit
        while d1 is not None or d2 is not None or c != 0:
            v1 = 0  # value 1
            if d1 is not None:
                v1 = d1.val
            v2 = 0  # value 2
            if d2 is not None:
                v2 = d2.val
            ds = v1 + v2 + c  # digit sum
            if ds < 10:  # no carry
                c = 0
            else:  # carry
                ds -= 10
                c = 1
            if fd:  # set the first digit
                rd.val = ds
                fd = False
            else:  # append the subsequent digits
                rd.next = ListNode(ds)
                rd = rd.next
            if d1 is not None:
                d1 = d1.next
            if d2 is not None:
                d2 = d2.next
        return r
