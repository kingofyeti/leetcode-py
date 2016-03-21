class ListNode(object):
  def __init__(self,x):
    self.val = x
    self.next = None

  def print_list(self,head):
    if head == None:
      return head
    ptr = head
    while (ptr != None):
      print ptr.val
      ptr = prt.next

  def make_list(self,lst):
    if len(lst) == 0:
      return None
    

class Solution(object):
  def m(self,head):
     

solution = Solution()
str_in = raw_input()
print solution.m()
