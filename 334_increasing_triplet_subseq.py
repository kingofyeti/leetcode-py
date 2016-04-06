import sys

class Solution(object):
  def increasingTriplet(self,nums):
    l1 = l2 = float('inf')
    if len(num) < 3: return False
    for i in nums:
      if i <= l1:
        l1 = i
      elif i <= l2:
        l2 = i
      else: return True
    return False


lst = map(int,raw_input().split())

solution = Solution()
print solution.increasingTriplet(lst)
