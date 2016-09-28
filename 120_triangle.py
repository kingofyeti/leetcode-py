class Solution(object):
  def minimumTotal(self,triangle):
    n = len(triangle)
    if n == 1: return triangle[0][0]
    res = [[0] * i for i in xrange(1,n+1)]
    res[0][0] = triangle[0][0]
    for i in xrange(1,n):
      for j in xrange(1,i):
        res[i][j] = min(res[i-1][j],res[i-1][j-1]) + triangle[i][j]
      res[i][0] = res[i-1][0] + triangle[i][0]
      res[i][i] = res[i-1][i-1] + triangle[i][i]
    return min(res[n-1])

triangle = []
while True:
  cur = raw_input() 
  if cur == '': break
  cur = map(int,cur.split())
  triangle += [cur]

solution = Solution()
print solution.minimumTotal(triangle)
