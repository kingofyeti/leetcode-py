import sys

class NumArray(object):
  def __init__(self,nums):
    self.lst = [0]
    for i in xrange(len(nums)):
      self.lst.append(self.lst[-1]+nums[i])

  def sumRange(self,i,j):
    return self.lst[j+1]-self.lst[i]

class Solution(object):
  def m(self):
    return

solution = Solution()
print solution.m()
