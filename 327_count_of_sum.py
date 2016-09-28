class Solution(object):
  def countRangeSum_trivial(self,nums,lower,upper):
    n = len(nums)
    if not nums: return 0 
    sum_lst = [0] * (n+1)
    res = 0
    for i in range(n):
      sum_lst[i+1] = sum_lst[i] + nums[i]

    for i in range(n):
      for j in range(i+1,n+1):
        sum_ij = sum_lst[j] - sum_lst[i]
        if sum_ij >= lower and sum_ij <= upper: 
          res += 1
    return res


  def countRangeSum(self,nums,lower,upper):
    
    return

solution = Solution()

nums = map(int,raw_input().split())
lower,upper = [int(x) for x in raw_input().split()]

print solution.countRangeSum(nums,lower,upper)
