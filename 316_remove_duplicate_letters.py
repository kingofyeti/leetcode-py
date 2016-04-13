class Solution(object):
  def removeDuplicateLetters(self,s):
    dic,is_inside = [0] * 26,[False] * 26
    c2i = lambda c: ord(c) - 97
    n = len(s)
    # ord('a') = 97
    for c in s:
      dic[c2i(c)] += 1
    res = ''
    for i in s:
      idx = ord(i)-97
      dic[idx] -= 1
      if is_inside[idx]: continue
      while res and dic[c2i(res[-1])] > 0 and res[-1] > i:
        is_inside[c2i(res[-1])] = False
        res = res[:-1]
      res += i
      is_inside[c2i(i)] = True
    return res
    
s = raw_input()
solution = Solution()
print solution.removeDuplicateLetters(s)
