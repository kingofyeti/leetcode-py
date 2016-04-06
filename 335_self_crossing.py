class Solution(object):
  def isSelfCrossing(self,x):
    if len(x) < 4: return False
    for i in range(0,len(x)-3):
      # Case 1:
      if i + 3 < len(x):
        if x[i] >= x[i+2] and x[i+1] <= x[i+3]:
          return True
      # Case 2:
      if i + 4 < len(x):
        if x[i] + x[i+4] >= x[i+2] and x[i+1] == x[i+3]:
          return True
      # Case 3:
      if i + 5 < len(x):
        if x[i] + x[i+4] >= x[i+2] and x[i+1] + x[i+5] >= x[i+3] and x[i+3] >= x[i+1] and x[i+4] <= x[i+2]:
          return True
    return False
    # Case 1: 
    #     _______
    #     |      |
    #     |______|___
    #            |
    #
    # Case 2: 
    #     ________
    #     |       |     
    #     |       |  
    #     |       | 
    #     |       |  
    #     |_______|
    #
    # Case 3: 
    #     ________
    #     |    ___|___     
    #     |       |   |
    #     |           | 
    #     |___________|
    #

solution = Solution()
str_in = raw_input()
lst = map(int,str_in.split())
print solution.isSelfCrossing(lst)
