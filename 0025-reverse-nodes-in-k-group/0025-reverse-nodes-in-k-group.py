class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # find the k-th node of this group
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # reverse the group; start with prev pointing at the next group
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnect: group_prev -> old kth (new head of group)
            old_head = group_prev.next  # this is now the tail of the reversed group
            group_prev.next = kth
            group_prev = old_head