import sys

class Solution(object):
  def isPowerOfFour(self,num):
    return ((len(bin(num)) % 2) == 1) and ((num & (num-1)) == 0) and num != 0

num = int(raw_input())
solution = Solution()
print solution.isPowerOfFour(num)
