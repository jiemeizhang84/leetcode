class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root