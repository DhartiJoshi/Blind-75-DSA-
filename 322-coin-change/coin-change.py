class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Step 1: Create DP array
        dp = [float('inf')] * (amount + 1)
        
        # Step 2: Base case
        dp[0] = 0
        
        # Step 3: Fill DP array
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Step 4: Return result
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]