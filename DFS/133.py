class Solution:
    
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return node
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))            
            return copy
        
        return dfs(node)