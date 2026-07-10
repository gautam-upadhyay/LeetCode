class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [1] + numWays
        ans = []
        
        for c in range(1, n + 1):
            if dp[c] == 0:
                continue

            if dp[c] != 1:
                return []
                
            ans.append(c)
    
            for s in range(n, c - 1, -1):
                dp[s] -= dp[s - c]
                
        return ans