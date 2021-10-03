class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(l):
            if l is None:
                return None
            prev = None
            while l:
                tmp = l.next
                l.next = prev
                prev = l
                l = tmp
            return prev
        
        rl1 = reverse(l1)
        rl2 = reverse(l2)
        carry = 0
        nex = None
        while rl1 or rl2 or carry:
            v1 = v2 = 0
            if rl1:
                v1 = rl1.val
                rl1 = rl1.next
            if rl2:
                v2 = rl2.val
                rl2 = rl2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            curr = ListNode(val)
            curr.next = nex
            nex = curr
        return curr  