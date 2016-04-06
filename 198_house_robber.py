class Solution(object):
  def rob(self,nums):
    if len(nums) == 0:
      return 0
    if len(nums) == 1:
      return nums[0]
    
    max_without_last = 0
    max_with_last = nums[0]
    res = 0
    
    for i in range(1,len(nums)):
      res = max(max_without_last + nums[i],max_with_last)
      max_without_last = max_with_last
      max_with_last = res
      
    return res

solution = Solution()
str_in = raw_input()
int_list = [int(i) for i in str_in.split(' ') if i.isdigit()]
print solution.rob(int_list)
