class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [root]
        total = 0
        
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None
        
        while stack:
            sub_root = stack.pop()
            if isLeaf(sub_root.left):
                total += sub_root.left.val
            if sub_root.right is not None:
                stack.append(sub_root.right)
            if sub_root.left is not None:
                stack.append(sub_root.left)
        return total

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def helper(sub_root, isLeft):
            if sub_root is None:
                return 0
            
            if sub_root.left is None and sub_root.right is None:
                return sub_root.val if isLeft else 0
            
            return helper(sub_root.left, True) + helper(sub_root.right, False)
        
        return helper(root, False)