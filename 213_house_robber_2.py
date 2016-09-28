class Solution(object):

  def rob(self,nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]

    return rob_with_range(nums,)

solution = Solution()
print solution.rob()
