import sys

class Solution(object):
  def helper(self,a,b,num):
    la = len(a)
    lb = len(b)
    lnum = len(num)
    ab = str(int(a)+int(b))
    lab = len(ab)
    if lab > (lnum - la - lb): return False
    c = num[(la+lb):(la+lb+lab)]
    if c == str(ab):
      if lnum == la+lb+lab: return True
      else:
        return self.helper(b,c,num[la:])
    else:
      return False

  def isAdditiveNumber(self,num):
    n = len(num)
    res = False
    if n < 3: return False
    for i in xrange(1,n):
      for j in xrange(i+1,n):
        if (num[:i][0] == '0' and len(num[:i])>1) or (num[i:j][0] == '0' and
len(num[i:j])
> 1): continue
        res |= self.helper(num[:i],num[i:j],num)
    return res

num = raw_input()
solution = Solution()
print solution.isAdditiveNumber(num)
