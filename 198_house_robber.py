class Solution(object):
  def rob(self,nums):
    if len(nums) == 0:
      return 0
    if len(nums) == 1:
      return nums[0]
    if len(nums) == 2:
      return max(nums[0],nums[1])
    res = [nums[0],max(nums[0],nums[1])]
    for i in range(2,len(nums)):
      res.append(max(nums[i]+res[i-2],res[i-1]))
    return res[len(nums)-1]
         

solution = Solution()
str_in = raw_input()
int_list = [int(i) for i in str_in.split(' ') if i.isdigit()]
print solution.rob(int_list)
