import sys

class Solution(object):
  def firstBadVersion(self,n):
    l,r = 1,n+1
    while l < r:
      mid = l + ((r-l) >> 1)
      if isBadVersion(mid):
        r = mid
      else:
        l = mid + 1
    return l

solution = Solution()
print solution.m()
