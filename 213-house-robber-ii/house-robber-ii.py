from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # If only one house
        if len(nums) == 1:
            return nums[0]
        
        # Helper function for normal House Robber (linear)
        def rob_linear(arr):
            prev1 = 0   # dp[i-1]
            prev2 = 0   # dp[i-2]
            
            for num in arr:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp
            
            return prev1
        
        # Case 1: Exclude last house
        case1 = rob_linear(nums[:-1])
        
        # Case 2: Exclude first house
        case2 = rob_linear(nums[1:])
        
        return max(case1, case2)