class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        next_level = [root, ]
        min_depth = 1
        while next_level:
            curr_level = next_level
            next_level = []
            for node in curr_level:
                if node.left is None and node.right is None:
                    return min_depth
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            min_depth += 1
        return min_depth