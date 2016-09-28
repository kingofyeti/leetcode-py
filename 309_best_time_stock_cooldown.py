import sys

class Solution(object):
  def maxProfit(self,prices):
    n = len(prices)
    if n == 0 or n == 1:  return 0
    have_stock = [0]*n
    no_stock = [0]*n
    have_stock[0] = -prices[0]
    have_stock[1] = max(-prices[0],-prices[1]) 
    no_stock[1] = max(0,prices[1]-prices[0])
    for i in xrange(2,n):
      # have_stock stores the current money you have if you buy ith day's stock
      # no_stock stores the current money you have if you did not buy ith
      # stock(you may sell stock this day)
      have_stock[i] = max(have_stock[i-1],no_stock[i-2]-prices[i])
      no_stock[i] = max(have_stock[i-1]+prices[i],no_stock[i-1])
    print have_stock,no_stock
    return no_stock[n-1]

prices = map(int,raw_input().split())
solution = Solution()
print solution.maxProfit(prices)
