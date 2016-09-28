class Solution(object):
  def wiggleSort(self,nums):
    nu = sorted(nums)
    half = len(nums[::2])
    # both two side has to be [::1], because the concatenate part may have problem
    nums[::2],nums[1::2] = nums[:half][::-1],nums[half:][::-1]

  

nums = map(int,raw_input().split())

solution = Solution()
print solution.wiggleSort(nums)
