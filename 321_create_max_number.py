import sys

class Solution(object):

  def maxNumber(self,nums1,nums2,k):
    def get_k_max(lst,k):  
      res,n = [],len(lst)
      if k == 0: return res
      for i in xrange(n):
        while res and res[-1] < lst[i] and (k - len(res)) < (n - i):
            res.pop(-1)
        if len(res) < k:
          res.append(lst[i])
      return res

    res = []
    for i in xrange(max(0,k-len(nums2)),min(k,len(nums1))+1 ):
      lst1 = get_k_max(nums1,i) 
      lst2 = get_k_max(nums2,k-i)
      cur = [max(lst1,lst2).pop(0) for _ in lst1+lst2]
      res = max(res,cur)
    return res 
    
    
k = int(raw_input())
nums1 = map(int,raw_input().split(' '))
nums2 = map(int,raw_input().split(' '))

solution = Solution()
print solution.maxNumber(nums1,nums2,k)
