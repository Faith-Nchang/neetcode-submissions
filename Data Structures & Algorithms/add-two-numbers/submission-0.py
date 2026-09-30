# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 12 / 10 = 1
# 12 % 10 = 2

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        d = ListNode(0)
        cur = d

        while l1 or l2 or carry:
            if not l1 and l2:
                # use just l2
                s = l2.val + carry
                carry = s // 10
                num = s % 10

                cur.next = ListNode(num)
                l2 = l2.next
                cur = cur.next
            elif not l2 and l1: # use just l2
                s = l1.val + carry
                carry = s // 10
                num = s % 10

                cur.next = ListNode(num)
                l1 = l1.next
                cur = cur.next
            elif l1 and l2: # use both
                s = l1.val + l2.val + carry
                carry = s // 10
                num = s % 10

                cur.next = ListNode(num)
                l1 = l1.next
                l2 = l2.next
                cur = cur.next
            else:
                
                cur.next = ListNode(carry)
                break
        return d.next


        