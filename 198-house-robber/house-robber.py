from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # If only one house
        if len(nums) == 1:
            return nums[0]
        
        # Create dp array
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill dp array
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # Last value contains answer
        return dp[-1]
