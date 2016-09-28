import sys

class Solution(object):
  def moveZeroes(self,nums):
    n = len(nums)
    nums = [i for i in nums if i != 0]
    nums = nums + [0] * (n - len(nums))
    return nums

nums = map(int,raw_input().split())

solution = Solution()
print solution.moveZeroes(nums)
