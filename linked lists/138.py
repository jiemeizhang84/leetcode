class Solution:
    def __init__(self):
        self.visited = {}
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        def copy_node(node):
            if node:
                if node in self.visited:
                    return self.visited[node]
                else:
                    self.visited[node] = Node(node.val, None, None)
                    return self.visited[node]
            return None
        
        if head is None:
            return None
        
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        
        while old_node:
            new_node.random = copy_node(old_node.random)
            new_node.next = copy_node(old_node.next)
            
            old_node = old_node.next
            new_node = new_node.next
            
        return self.visited[head]