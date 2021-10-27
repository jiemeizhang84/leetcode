class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            size = len(queue)
            level_sum = 0
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_avg = level_sum / size
            result.append(level_avg)
        return result