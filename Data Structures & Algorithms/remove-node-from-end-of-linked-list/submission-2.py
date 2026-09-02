# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length  = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        
        cur = head
        if (length - n) == 0:
            return head.next

        i = 0
        while i < (length - 1):
            if  (i + 1) == (length - n):
                cur.next = cur.next.next
                break
            cur = cur.next
            i += 1

        return head

        
