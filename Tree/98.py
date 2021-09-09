class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        
        self.prev = -math.inf
        return inorder(root)