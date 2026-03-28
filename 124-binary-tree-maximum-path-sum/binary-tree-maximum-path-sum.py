class Solution:
    def maxPathSum(self, root):
        
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # get max from left and right (ignore negatives)
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # case 1: path passing through this node
            current_sum = left + node.val + right
            
            # update global max
            self.max_sum = max(self.max_sum, current_sum)
            
            # case 2: return to parent (only one side)
            return node.val + max(left, right)
        
        dfs(root)
        return self.max_sum