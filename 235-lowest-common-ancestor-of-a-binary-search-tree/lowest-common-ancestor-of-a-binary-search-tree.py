class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while root:
            
            # If both nodes are smaller, go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # If both nodes are greater, go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # Otherwise, this is the split point → LCA found
            else:
                return root