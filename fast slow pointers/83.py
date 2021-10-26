class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head
        curr = head.next if head else None
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head