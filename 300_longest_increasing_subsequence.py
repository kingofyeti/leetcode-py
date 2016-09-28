import sys

class Solution(object):
  def lengthOfLIS_naive(self,nums):
    n = len(nums)
    if n == 0 : return 0
    lst = [1] * n
    for i in xrange(1,n):
      for j in xrange(i):
        if nums[j] < nums[i]:
          lst[i] = max(lst[i],lst[j]+1)
    return max(lst)

  def lengthOfLIS(self,nums):

nums = map(int,raw_input().split())
solution = Solution()
print solution.lengthOfLIS(nums)
