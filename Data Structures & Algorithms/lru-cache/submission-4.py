class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.oldest = Node(-1, -1)
        self.newest = Node(-1, -1)

        self.oldest.next = self.newest
        self.newest.prev = self.oldest


    def deleteNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def addNode(self, node):
        node.next = self.newest
        node.prev = self.newest.prev

        self.newest.prev.next = node
        self.newest.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.deleteNode(node)
        self.addNode(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]

            node.val = value

            self.deleteNode(node)
            self.addNode(node)

        else:
            node = Node(key, value)

            self.cache[key] = node
            self.addNode(node)

            if len(self.cache) > self.capacity:
                node = self.oldest.next

                self.deleteNode(node)
                del self.cache[node.key]