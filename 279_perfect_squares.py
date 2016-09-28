import sys
import math

class Solution(object):
  def numSquares_naive(self,n):
    if n <= 1: return n
    max_sqrt = int(math.sqrt(n))
    lst = [i*i for i in xrange(1,max_sqrt+1)] 
    res_lst = [n+1] * (n+1)
    for x in lst:
      res_lst[x] = 1
    for i in xrange(1,n+1):
      for j in lst:
        if j < i:
          res_lst[i] = min(res_lst[i-j]+1,res_lst[i])
        else:
          break
    return res_lst[n] 

    numSquaresDP = [0]
    def numSquares_maybe_good(self, n):
        if len(self.numSquaresDP) <= n:
            perfectSqr = [v**2 for v in xrange(1, int(math.sqrt(n)) + 1)]
            for i in xrange(len(self.numSquaresDP), n + 1):
                self.numSquaresDP.append( min(1 + self.numSquaresDP[i - sqr] for sqr in perfectSqr if sqr <= i))
        return self.numSquaresDP[n]  


n = int(raw_input())
solution = Solution()
print solution.numSquares(n)
