class Solution(object):
  def coinChange(self,coins,amount):
    res = [0] + [float('inf')] * (amount)
    for k in coins:
      for j in range(k,amount+1):
        res[j] = min(res[j-k] + 1,res[j])
    return res[amount]==float('inf') and -1 or res[amount]

coins = [2,6]
amount = 11

solution = Solution()
print solution.coinChange(coins,amount)
