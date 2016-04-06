class Solution(object):

  def longestIncreasingPath(self,matrix):
    if not matrix: return 0
    row,col = len(matrix),len(matrix[0])
    cur_map = [[0] * col for i in range(row)]

    return max([self.dfs(i,j,row,col,matrix,cur_map) for i in range(row) for j in range(col)])

  def dfs(self,i,j,row,col,matrix,cur_map):
    # already visited ---> not 0
    if cur_map[i][j] != 0: return cur_map[i][j]
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
      ni,nj = i+di,j+dj
      if ni >= 0 and ni < row and nj >=0 and nj < col and matrix[ni][nj] < matrix[i][j]:
        cur_map[i][j] = max(cur_map[i][j],self.dfs(ni,nj,row,col,matrix,cur_map))
    cur_map[i][j] += 1
    return cur_map[i][j]


solution = Solution()
matrix = []

Done = False
while True:
  oneline = raw_input()
  if oneline != '':
    matrix += [map(int,oneline.split())]
  else: break

print solution.longestIncreasingPath(matrix)
