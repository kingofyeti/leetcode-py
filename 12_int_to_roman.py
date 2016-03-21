class Solution(object):
  def intToRoman(self,num):
    res = ''
    symbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    i = 0
    while (i < len(val)):
      if num < val[i]:
        i += 1 
      else:
        res = res + symbol[i]
        num = num - val[i]
    return res
         
      
    
    
solution = Solution()
str_in = raw_input()
print solution.intToRoman(int(str_in))
