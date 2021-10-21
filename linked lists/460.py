class DLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = key
        self.freq = 1
        self.prev = None
        self.next = None
        
class DLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def __len__(self):
        return self.size
    
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
        
    def _remove_node(self, node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
    def _pop_tail(self):

        node = self.tail.prev
        self._remove_node(node)
        
        return node
        

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minfreq = 0
        self.nodemap = {}
        self.freqmap = collections.defaultdict(DLinkedList)

    def freq_update(self, node):
        nodelist = self.freqmap[node.freq]
        nodelist._remove_node(node)
        
        if nodelist.size == 0 and self.minfreq == node.freq:
            self.minfreq += 1
            

        node.freq += 1
        new_nodelist = self.freqmap[node.freq]
        new_nodelist._add_node(node)
        
    def get(self, key: int) -> int:
        if key not in self.nodemap:
            return -1
        
        node = self.nodemap[key]
        self.freq_update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodemap:
            node = self.nodemap[key]
            self.freq_update(node)
            node.value = value
        else:
            if self.size == self.capacity:
                
                node = self.freqmap[self.minfreq]._pop_tail()
                
                del self.nodemap[node.key]
                self.size -= 1
            node = DLinkedNode()
            node.key = key
            node.value = value
            
            self.nodemap[key] = node
            self.freqmap[node.freq]._add_node(node)
            self.minfreq = 1
            
            self.size += 1