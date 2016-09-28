import sys

class TreeNode(object):
    def __init__(self,x):
      self.val = x
      self.left = None
      self.right = None

class Codec:
    def serialize(self,root):
      if not root: return None
      queue = [root]
      self.res = []
      while queue:
        cur = queue.pop(0)
        if cur != 'null':
          self.res.append(cur.val) 
        else:
          self.res.append('null')
          continue
        if cur.left: 
          queue.append(cur.left)
        else:
          queue.append('null')
        if cur.right: 
          queue.append(cur.right)
        else:
          queue.append('null')
      return
    
    def deserialize(self,data):
      return

class Solution(object):
  def m(self):
    return

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

codec = Codec()
codec.serialize(t1);
print codec.res

solution = Solution()
print solution.m()
