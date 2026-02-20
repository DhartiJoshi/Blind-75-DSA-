class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Base case: if tree is empty
        if root is None:
            return None
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert left subtree
        self.invertTree(root.left)
        
        # Recursively invert right subtree
        self.invertTree(root.right)
        
        # Return root
        return root