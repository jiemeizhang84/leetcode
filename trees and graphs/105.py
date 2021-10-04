class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def array_to_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, val_ind_map[root_value] - 1)
            root.right = array_to_tree(val_ind_map[root_value] + 1, right)
            return root
                            
        val_ind_map = {}
        for ind, value in enumerate(inorder):
            val_ind_map[value] = ind
        preorder_index = 0
        
        return array_to_tree(0, len(preorder) - 1)