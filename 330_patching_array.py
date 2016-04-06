class Solution(object):
  def minPatches(self,nums,n):
    i = res = 0
    max_num = 1
    while(max_num <= n):
      if i < len(nums) and nums[i] <= max_num:
        max_num += nums[i]
        i += 1
      else:
        # max_num > nums[i]
        max_num <<= 1
        res += 1
    return res

solution = Solution()
nums = map(int,raw_input().split())
n = int(raw_input())

print nums,n
print solution.minPatches(nums,n)
