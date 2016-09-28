class TreeNode(object):
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def _rob_helper(self,node):
    if not node: return (0,0)
    # not robbed, robbed
    l1,l2 = self._rob_helper(node.left)
    r1,r2 = self._rob_helper(node.right)
    return (max(l1,l2)+max(r1,r2),l1+r1+node.val)
      
  def rob(self,root):
    return max(self._rob_helper(root))

solution = Solution()
solution.rob()
