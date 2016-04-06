import collections

class Solution(object):
  def findItinerary(self,tickets):
    mymap = collections.defaultdict(list)
    res = []
    n = len(tickets)
    for ticket in tickets:
      mymap[ticket[0]] += [ticket[1]]
    get = self.dfs('JFK',res,mymap,0,n)
    return get == True and res

  def dfs(self,cur,res,mymap,i,n):
    if len(res) == n: 
      res.append(cur)
      return True;
    d = sorted(mymap[cur])
    for des in d:
        res.append(cur)
        # important: should remove what you add!
        mymap[cur].remove(des)
        get = self.dfs(des,res,mymap,i+1,n)
        if not get:
          mymap[cur].append(des)
          res.pop(-1)
        else:
          return True
    

      

solution = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

print solution.findItinerary(tickets)
