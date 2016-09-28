import sys

class NumMatrix(object):
  def __init__(self,matrix):
    if len(matrix) == 0: return
    self.row,self.col = len(matrix), len(matrix[0])
    self.sum_mat = [[0] * (self.col+1) for i in xrange(self.row+1)]
    for i in xrange(1,self.row+1):
      for j in xrange(1,self.col+1):
        self.sum_mat[i][j] = self.sum_mat[i][j-1] + self.sum_mat[i-1][j] - self.sum_mat[i-1][j-1] + matrix[i-1][j-1]  

  def sumRegion(self,row1,col1,row2,col2):
    return self.sum_mat[row2+1][col2+1] + self.sum_mat[row1][col1] -self.sum_mat[row2+1][col1] - self.sum_mat[row1][col2+1]

class Solution(object):
  def m(self):
    return

#matrix = [
#  [3, 0, 1, 4, 2],
#  [5, 6, 3, 2, 1],
#  [1, 2, 0, 1, 5],
#  [4, 1, 0, 1, 7],
#  [1, 0, 3, 0, 5]
#]

matrix = [[-1]]

t = NumMatrix(matrix)
print t.sumRegion(0,0,0,0)
solution = Solution()
print solution.m()
