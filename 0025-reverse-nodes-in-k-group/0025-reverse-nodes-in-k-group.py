class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Step 1: Check if k nodes exist
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes
            
            group_next = kth.next  # node after kth

            # Step 2: Reverse k nodes
            prev, curr = group_next, prev_group.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 3: Reconnect
            temp = prev_group.next
            prev_group.next = prev
            prev_group = temp
