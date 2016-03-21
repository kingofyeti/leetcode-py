class Solution(object):
  def romanToInt(self,s):
    res = 0
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    prev = d[s[0]]
    res += prev
    for ch in s[1:]:
      cur = d[ch]
      if cur <= prev:
        res += cur
      else:
        res += cur - 2 * prev
      prev = cur
    return res

solution = Solution()
str_in = raw_input()
print solution.romanToInt(str_in)
