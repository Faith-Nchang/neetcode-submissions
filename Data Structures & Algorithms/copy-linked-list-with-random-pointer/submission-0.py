"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)

        cur = dummy
        old_to_new = {}
        while head:
            cur.next = Node(x=head.val)
            old_to_new[head] = cur.next
            head = head.next
            cur = cur.next

        for old_node, new_node in old_to_new.items():
            old_random = old_node.random
            if old_random:
                new_random = old_to_new[old_random]

                new_node.random = new_random
            else:
                new_node.random = None

        return dummy.next
        