import sys

class Solution(object):
  def getHint(self,secret,guess):
    n = len(secret)
    l1 = [0] * 10
    l2 = [0] * 10
    a,b = 0,0
    for i in xrange(n):
      l1[ord(secret[i])-ord('0')] += 1
      l2[ord(guess[i])-ord('0')] += 1
    for i in xrange(n):
      if secret[i] == guess[i]:
        a += 1
        l1[ord(secret[i])-ord('0')] -= 1
        l2[ord(guess[i])-ord('0')] -= 1
    b = sum(min(l1[i],l2[i]) for i in xrange(10))
    return str(a)+'A'+str(b)+'B'
      

secret = raw_input()
guess = raw_input()
solution = Solution()
print solution.getHint(secret,guess)
