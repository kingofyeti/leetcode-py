class Solution(object):
  def maxProduct(self,words):
    n = len(words)
    box = [0] * n
    for i,v in enumerate(words):
      for j in v:
        # using '|' for each letter
        # if we have duplicate letter, '|' will not effect them
        box[i] |= 1 << ord(j)-ord('a') 

    res_max = 0;
    for i in range(n):
      # if use i+1 is better!
      for j in range(i+1,n):
        if not box[i] & box[j]:
          res_max = max(res_max,len(words[i]) * len(words[j]))

    return res_max

  def three_line(self,words):
    # it tells me how to use map, reduce and lambda...
    lst = map(lambda word: reduce(lambda x, y: x | y, [1 << (ord(c) - ord('a')) for c in word], 0) , words)
    ret = [len(words[i]*len(words[j]) for i in xrange(len(lst)) for j in xrange(i+1,len(lst))if not lst[i]&lst[j]  )]
    return max(ret) if ret else 0



words = raw_input().split()

solution = Solution()
print solution.maxProduct(words)
