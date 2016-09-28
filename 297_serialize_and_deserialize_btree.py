import sys

class TreeNode(object):
  def __init__(self,x):
    self.val = x
    self.left = None
    self.right = None

class Codec:
  def serialize(self,root):
    res = []
    if not root:  return res
    lst = [root]
    while lst:
      node = lst.pop(0)
      if node == '#':
        res.append('#')
        continue
      else:
        res.append(node.val)
      if node.left:
        lst.append(node.left)
      else:
        lst.append('#')
      if node.right:
        lst.append(node.right)
      else:
        lst.append('#')
    return res

  def deserialize(self,data):
    head = None
    if not data: return head
    head = TreeNode(data.pop(0))
    lst = [head]
    while lst:
      t = lst.pop(0)
      l = TreeNode(data.pop(0))
      r = TreeNode(data.pop(0))
      if l.val == '#':
        t.left = None
      else:
        t.left = l
        lst.append(l)
      if r.val == '#':
        t.right = None
      else:
        t.right = r
        lst.append(r)
    return head

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
lst = codec.serialize(t1)
print lst
h = codec.deserialize(lst)
print codec.serialize(h)


solution = Solution()
print solution.m()
