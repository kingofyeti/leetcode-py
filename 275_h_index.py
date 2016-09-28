import sys

class Solution(object):
  def hIndex(self,citations):
    l,r,n = 0,len(citations),len(citations)
    while l<r:
      mid = (l+r) >> 1
      if n - mid <= citations[mid]:
        r = mid
      else:
        l = mid+1 
    return n-l

citations = map(int,raw_input().split())

solution = Solution()
print solution.hIndex(citations)
