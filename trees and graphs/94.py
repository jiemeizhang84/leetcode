class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
              
        def helper(root, traversal):
            if root is None:
                return

            helper(root.left, traversal)
            traversal.append(root.val)
            helper(root.right, traversal)
        
        result = []
        helper(root, result)
        return result


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result