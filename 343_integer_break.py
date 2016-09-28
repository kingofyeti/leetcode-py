import sys

class Solution(object):
  def integerBreak(self,n):
    if n <= 3: return n-1
    mod = n % 3
    if mod == 0:
      return pow(3,n/3)
    if mod == 1:
      return pow(3,n/3-1)*4
    if mod == 2:
      return pow(3,n/3)*2

n = int(raw_input())
solution = Solution()
print solution.integerBreak(n)
