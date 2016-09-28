import sys

class Solution(object):
  def wordPattern(self,pattern,str):
    lst = str.split()
    
    if len(lst) != len(pattern): return False
    n = len(lst)
    map_1, map_2 = {},{}
    for i in xrange(n):
      if map_1.get(pattern[i],-1) != map_2.get([lst[i],-1):
        return False
      map_1[pattern[i]] = map_2[lst[i]] = i
   return True 

solution = Solution()
str = raw_input()
pattern = raw_input()
print solution.wordPattern(pattern,str)
