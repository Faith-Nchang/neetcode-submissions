# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # count nodes
        nodes = 0
        cur = head
        while cur:
            nodes += 1
            cur = cur.next
        
        if nodes == n: # first element
            return head.next
        
        cur = head
        i = 1
        while i < (nodes - n):
            cur = cur.next
            i += 1
        if n == 1:
            cur.next = None
            return head

        cur.next = cur.next.next
        return head




        