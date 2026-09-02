# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # reverse the second half
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        dummy = ListNode(0)
        merged = dummy
        flag = True

        while head and prev:
            if flag:
                merged.next = head
                head = head.next
            else:
                merged.next = prev
                prev = prev.next
            merged = merged.next
            flag = not flag

        # Attach any leftover nodes
        if head:
            merged.next = head
        elif prev:
            merged.next = prev
        else:
            merged.next = None

        
        

        head = dummy.next

        