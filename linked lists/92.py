class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftprev, cur = dummy, head
        for _ in range(left - 1):
            leftprev, cur = cur, cur.next
        
        prev = None
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
            
        leftprev.next.next = cur
        leftprev.next = prev