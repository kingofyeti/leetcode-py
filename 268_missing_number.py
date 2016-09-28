import sys

class Solution(object):
  def missingNumber(self,nums):
    return ((len(nums) * (len(nums) + 1)) >> 1) - sum(nums)

nums = map(int,raw_input().split())

solution = Solution()
print solution.missingNumber(nums)
