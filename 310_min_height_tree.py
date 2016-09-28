import sys

class Solution(object):
  def findMinHeightTrees_naive(self,n,edges):
    graph = [[] for i in xrange(n)]
    res = [i for i in xrange(n)] 
    for e in edges:
      graph[e[0]] += [e[1]] 
      graph[e[1]] += [e[0]] 
    
    # Ugly, because you dont have to cut the graph
    # you can cut the # of node connected
    while len(res) > 2:
      leaf = [i for i,v in enumerate(graph) if len(v) == 1]
      for i in leaf:
        a,b = i,graph[i][0]
        graph[a].remove(b)
        graph[b].remove(a)
        res.remove(i)
    return res

  def findMinHeightTrees(self,n,edges):
    if n == 1: return [0]
    graph = [[] for i in xrange(n)]
    degree = [0] * n
    for x,y in edges:
      graph[x].append(y) 
      graph[y].append(x) 
      degree[x] += 1 
      degree[y] += 1 
    
    leaf = [i for i in xrange(len(degree)) if degree[i] == 1]
    num = n
    while num > 2:
      cur = [] 
      for i in leaf:
          degree[i] = 0
          num -= 1
          for j in graph[i]:
            degree[j] -= 1
            if degree[j] == 1:
              cur.append(j)
      leaf = cur
    return leaf
          

edges = []
n = int(raw_input())
for line in sys.stdin:
  edges += [map(int,line.split())]

solution = Solution()
print solution.findMinHeightTrees(n,edges)
