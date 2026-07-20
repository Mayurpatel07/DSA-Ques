class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def append_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def remove_tail(self):
        if self._size == 0:
            return None
        tail_node = self.tail.prev
        self.remove(tail_node)
        return tail_node

    def __len__(self):
        return self._size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key -> Node
        self.freq_map = {}  # Maps frequency -> DoublyLinkedList
        self.min_freq = 0  # Keeps track of the lowest frequency

    def _update_frequency(self, node: Node):
        old_freq = node.freq
        new_freq = old_freq + 1
        node.freq = new_freq

        # Remove node from its old frequency list
        self.freq_map[old_freq].remove(node)

        # If the old frequency list is empty and was the min_freq, increment min_freq
        if old_freq == self.min_freq and len(self.freq_map[old_freq]) == 0:
            self.min_freq += 1

        # Add node to its new frequency list
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DoublyLinkedList()
        self.freq_map[new_freq].append_front(node)

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.cache:
            return -1

        node = self.cache[key]
        self._update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_frequency(node)
        else:
            # Evict if cache is at maximum capacity
            if len(self.cache) >= self.capacity:
                # Evict the least recently used node from the minimum frequency list
                lru_node = self.freq_map[self.min_freq].remove_tail()
                if lru_node:
                    del self.cache[lru_node.key]

            # Create a brand new node with an initial frequency of 1
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.min_freq = 1

            if 1 not in self.freq_map:
                self.freq_map[1] = DoublyLinkedList()
            self.freq_map[1].append_front(new_node)
