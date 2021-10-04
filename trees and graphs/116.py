class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                curr = q.popleft()
                
                if i < level_size - 1:
                    curr.next = q[0]
                    
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
        return root