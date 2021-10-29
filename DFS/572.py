class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.same_tree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))        
        
    def same_tree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self.same_tree(r.left, s.left) and self.same_tree(r.right, s.right))
        return False