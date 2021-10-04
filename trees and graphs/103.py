class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, level):            
            if node is None:
                return []
            if len(level_list) == level:
                level_list.append(deque([]))
            if level % 2 == 0:
                level_list[level].append(node.val)
            else:
                level_list[level].appendleft(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
                            
        level_list = []
        helper(root, 0)
        return level_list