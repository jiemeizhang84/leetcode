class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root,])
        right_side = []
        
        while next_level:
            current_level = next_level
            next_level = deque()
            
            while current_level:
                node = current_level.popleft()
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            right_side.append(node.val)
            
        return right_side

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = deque([root,])
        right_side = []
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    right_side.append(node.val)
                    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return right_side

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        right_side = []
        
        def helper(node, level: int):
            if level == len(right_side):
                right_side.append(node.val)
                
            for child in [node.right, node.left]:
                if child:
                    helper(child, level + 1)
                    
        helper(root, 0)
        return right_side