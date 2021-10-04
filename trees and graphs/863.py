class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
                
        dfs(root)
        
        queue = deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nb in (node.left, node.right, node.parent):
                if nb and nb not in seen:
                    seen.add(nb)
                    queue.append((nb, d+1))
        return []