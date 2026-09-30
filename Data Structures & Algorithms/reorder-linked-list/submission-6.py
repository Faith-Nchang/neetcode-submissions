# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        n = 0
        cur = head

        while cur:
            n += 1
            cur = cur.next

        # split list
        i = 0
        cur = head
        prev = None

        while i < (n // 2):
            prev = cur
            cur = cur.next
            i += 1

        prev.next = None

        # reverse second half
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # merge
        left_cur = head
        right_cur = prev

        flag = 1
        dummy = ListNode(0)
        cur = dummy

        while left_cur and right_cur:
            if flag:
                cur.next = left_cur
                cur = left_cur
                left_cur = left_cur.next
                flag = 0
            else:
                cur.next = right_cur
                cur = right_cur
                right_cur = right_cur.next
                flag = 1

        if left_cur:
            cur.next = left_cur

        if right_cur:
            cur.next = right_cur