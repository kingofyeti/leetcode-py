import sys

class Solution(object):
  def nthSuperUglyNumber(self,n,prime):
    k = len(prime)
    lst = [0] * k
    res = [1]
    for i in range(1,n):
      cur_min = sys.maxint
      for c in range(k):
        cur_min = min(cur_min, res[lst[c]] * prime[c])
      res += [cur_min]
      for i in range(k):
        if res[-1] == prime[i] * res[lst[i]]:
          lst[i] += 1
    return res[-1]

n = int(raw_input())
primes = map(int,raw_input().split())
solution = Solution()
print solution.nthSuperUglyNumber(n,primes)
