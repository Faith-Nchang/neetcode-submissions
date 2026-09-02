# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        def merge_sorted_list(list_1, list_2):
            dummy = ListNode(0)
            cur = dummy
            while list_1 and list_2:
                if list_1.val <= list_2.val:
                    cur.next = list_1
                    cur = list_1
                    list_1 = list_1.next

                else:
                    cur.next = list_2
                    cur = list_2
                    list_2 = list_2.next
            if list_1:
                cur.next = list_1
            elif list_2:
                cur.next = list_2
            return dummy.next
        
        merged = None
        for linked_list in lists:
            merged = merge_sorted_list(merged, linked_list)
        return merged

       