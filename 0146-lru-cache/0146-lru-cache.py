class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Maps key -> Node
        
        # Dummy head and tail nodes to simplify insertions and deletions
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark it as recently used
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            # Check if we need to evict the least recently used item
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            # Create a new node and add it to the front
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node

    # Helper function to remove a node from the linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function to add a node right after the dummy head
    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

