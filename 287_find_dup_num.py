import sys

class Solution(object):
  def findDuplicate(self,nums):
    n = len(nums)-1
    l,r = 1,n
    while (l<=r):
      m = (l+r) >> 1
      l_num = sum([1 for x in nums if x <= m])
      if l_num <= m: 
        l = m + 1
      else:
        r = m - 1
    return l

nums = map(int,raw_input().split())

solution = Solution()
print solution.findDuplicate(nums)
