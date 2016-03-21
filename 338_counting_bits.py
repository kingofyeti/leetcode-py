class Solution(object):
  def countBits(self,num):
    res = [0] * (num+1)
    res[0] = 0
    for i in range(1,num+1):
      res[i] = res[i>>1] + i%2
    return res
      

solution = Solution()
str_in = raw_input()
print solution.countBits(int(str_in))
