class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # An empty tree is balanced and has a height of 0
            if not node:
                return 0
            
            # Check the left subtree
            left = dfs(node.left)
            if left == -1: 
                return -1
                
            # Check the right subtree
            right = dfs(node.right)
            if right == -1: 
                return -1
            
            # If the current node is unbalanced, pass -1 up the chain
            if abs(left - right) > 1:
                return -1
                
            # Otherwise, return the actual height of this node's subtree
            return 1 + max(left, right)
            
        # If the helper function returns -1, it means it's unbalanced
        return dfs(root) != -1