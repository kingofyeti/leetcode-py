import sys

class Iterator(object):
  def __init__(self,nums):
    self.lst = nums
  def hasNext(self):
    
  def next(self):
     
class PeekingIterator(object):
  def __init__(self,iterator):
    self.iterator = iterator
    self.nextVal = self.iterator.next()

  def peek(self):
    return self.nextVal
    
  def next(self):
    val = self.nextVal 
    self.nextVal = self.iterator.next() if self.iterator.hasNext() else None
    return val

  def hasNext(self):
    return False if self.nextVal == None else True

class Solution(object):
  def m(self):
    return

solution = Solution()
print solution.m()
