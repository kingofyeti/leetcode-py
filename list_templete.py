class ListNode:
  def __init__(self,x):
    self.val = x
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def __init__(self,node):
    self.head = node

  def add_node(self,data):
    node = ListNode(data)
    node.next = self.head
    self.head = node

  def print_list(self):
    if self.head == None: return
    ptr = self.head
    while (ptr != None):
      print ptr.val,
      ptr = ptr.next
    return

  def make_list(self,lst):
    if len(lst) == 0: return None
    while(len(lst)>0):
      val = lst.pop()
      self.add_node(val)
    return self.head

  def reverse_list(self):
    head = self.head
    res = None
    ptr = head
    while ptr != None:
      tmp = ptr.next
      ptr.next = res
      res = ptr
      ptr = tmp
    self.head = res
      
class Solution(object):
  def m(self):
    return
     
solution = Solution()
#str_in = raw_input()

#print solution.m()
