import sys

class NumArray(object):
  def __init__(self,nums):
    self.lst = list(nums)
    
  def update(self,i,val):  
    self.lst[i] = val
  
  def sumRange(self,i,j):
    return sum(self.lst[i:j+1])

class Solution(object):
  def m(self):
    return

solution = Solution()
print solution.m()
