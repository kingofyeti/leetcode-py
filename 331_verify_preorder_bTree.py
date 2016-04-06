from collections import deque

class TreeNode(object):
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class Tree:
  def __init__(self,node = None):
    self.root = node
   
  def make_tree(self,lst):
    if not lst: return
    self.root = TreeNode(lst.pop(0))
    root = self.root
    q = deque([root])
    while lst:
      node = q.popleft()
      cur = lst.pop(0)
      cur = cur == '#' and None or cur
      if not node.left: 
        node.left = TreeNode(cur)
        q.append(node.left)
      if not lst: break
      cur = lst.pop(0)
      cur = cur == '#' and None or cur
      if not node.right: 
        node.right = TreeNode(cur)
        q.append(node.right)

  def level_order(self):
    root = self.root
    if not root: return
    q = deque([root])
    while q:
      node = q.popleft()
      print node.val,
      if node.left: q.append(node.left)
      if node.right: q.append(node.right)

  def pre_order(self,node = 'root'):
    if not node: return
    if node == 'root':node = self.root
    print node.val,
    self.pre_order(node.left)
    self.pre_order(node.right)

  def in_order(self,node = 'root'):
    if not node: return
    if node == 'root':node = self.root
    self.in_order(node.left)
    print node.val,
    self.in_order(node.right)

  def post_order(self,node = 'root'):
    if not node: return
    if node == 'root':node = self.root
    self.post_order(node.left)
    self.post_order(node.right)
    print node.val,

class Solution(object):
  def isValidSerialization(self,preorder):
    stack = []
    for x in preorder.split(','):
      stack += [x]
      while len(stack) >= 3 and stack[-2:] == ['#','#'] and stack[-3].isdigit():
        stack = stack[:-3] + ['#']
    
    return stack == ['#']

solution = Solution()
tree = Tree()
s = '9,3,4,#,#,1,#,#,2,#,6,#,#'

print '\n',solution.isValidSerialization(s)
