import sys

class Solution(object):
  def countNumbersWithUniqueDigits(self,n):
    if n == 0:  return 1
    if n == 1:  return 10
    if n > 10:  return self.countNumbersWithUniqueDigits(10)
    i = n    
    res = 9
    # res(n) = res(n-1) + 9 * 9 * 8 ...(11-n)
    while i > 1:
      res *= 11 - i 
      i -= 1
    return res + self.countNumbersWithUniqueDigits(n-1)

solution = Solution()
n = 3
print solution.countNumbersWithUniqueDigits(n)
