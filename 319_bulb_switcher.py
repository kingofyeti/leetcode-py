class Solution(object):
  def bulbSwitch(self,n):
    # sqrt(n)
    if n == 0: return 0;
    res,i = 0,1
    while(i * i <= n):
      res += 1;
      i += 1
    return res

n = 16
solution = Solution()
print solution.bulbSwitch(n)
