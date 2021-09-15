class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(node, parentSum):
            if not node:
                return 0
            parentSum = parentSum * 2 + node.val
            if not node.left and not node.right:
                return parentSum            
            return helper(node.left, parentSum) + helper(node.right, parentSum)
        
        if not root:
            return 0
        return helper(root, 0)

class Solution:
      
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, current):
            nonlocal result
            if node:
                current = current * 2 + node.val
                if not node.left and not node.right:
                    result += current
                dfs(node.left, current)
                dfs(node.right, current)
        
        result = 0
        dfs(root, 0)
        return result

