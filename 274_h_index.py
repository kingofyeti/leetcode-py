import sys

class Solution(object):
  def hIndex(self,citations):
    if not citations: return 0
    return [min(i+1,c) for i,c in enumerate(sorted(citations,reverse=True))]

citations = map(int,raw_input().split())

solution = Solution()
print solution.hIndex(citations)
