class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        mid = self.get_mid(head)
        right = mid.next
        mid.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge_list(left, right)
    
    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge_list(self, left, right):
        dummy = node = ListNode()
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        if left:
            node.next = left
        if right:
            node.next = right
        return dummy.next