class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def dfs(node):
            if not node:
                return -1
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            diameter[0] = max(diameter[0], left_height + right_height + 2)
            return max(left_height, right_height) + 1
        
        dfs(root)
        return diameter[0]