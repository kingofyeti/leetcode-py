class Solution(object):
  def isPowerOfThree(self,n):
    if n <= 0: return False
    if n == 1: return True
    return self.isPowerOfThree(n / 3) and n % 3 == 0

  def isPowerOfThree_log(self,n):
    return n<=0 and False or n == round(3 ** round(math.log(n,3)))

solution = Solution()

d = int(raw_input())

print solution.isPowerOfThree(d)
