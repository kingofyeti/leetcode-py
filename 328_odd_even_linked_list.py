class ListNode:
  def __init__(self,x):
    self.val = x
    self.next = None

class LinkedList:
  def __init__(self,node = None):
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
  def oddEvenList(self,head):
    if head == None or head.next == None:
      return head
    odd = ListNode(-1)
    even = ListNode(-1)
    ptr_odd = odd
    ptr_even = even
    ptr = head
    sign = False
    while(ptr != None):
      if (sign == False):
        ptr_odd.next = ptr
        ptr_odd = ptr_odd.next
      else:
        ptr_even.next = ptr
        ptr_even = ptr_even.next
      ptr = ptr.next
      sign = not sign
    
    ptr_odd.next = even.next
    ptr_even.next = None
    return odd.next
     
solution = Solution()
str_in = raw_input()
lst = LinkedList();
lst.make_list([1,2,3])
lst.print_list()
res =  solution.oddEvenList(lst.head)

res_lst = LinkedList(res)
print '\nRes: ',res_lst.print_list()
