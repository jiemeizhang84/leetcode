class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next