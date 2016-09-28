#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <algorithm>

#define INT_MAX 0x7fffffff
#define INT_MIN 0x80000000

using namespace std;

void dfs(string cur,vector<string> &res, unordered_map<string,multiset<string>> &my_map){
  while(my_map[cur].size()){
    string next = *got->second.begin();
    got->second.erase(got->second.begin());
    dfs(next,res,my_map);  
  }
  res.push_back(cur);
}

vector<string> findItinerary(vector<pair<string,string>> tickets){
  unordered_map<string, multiset<string>> my_map;
  vector<string> res;
  string init = "JFK";
  for(auto ticket : tickets){
    my_map[ticket.first].insert(ticket.second); 
  }
  dfs(init,res,my_map);
  reverse(res.begin(),res.end());
  return res;
}


int main(){

}
