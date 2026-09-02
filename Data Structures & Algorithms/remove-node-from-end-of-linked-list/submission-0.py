# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        N = 0
        cur = head
        while cur:
            N+=1
            cur = cur.next
        
        
        
        i = 0
        prev = None
        cur = head
        while i < N - n:
            prev = cur
            cur = cur.next
            i += 1
        if head == cur:
            return head.next
        else:
            prev.next = cur.next
            return head
