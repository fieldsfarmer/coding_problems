#include <unordered_map>
#include <vector>

// directed graph
// basic setting follows 207. Course Schedule from leetcode
// Need 3 color, -1 processing; 0 not yet processing; 1 done processing




// undirected graph
// setting follows 261 Graph Valid Tree from leetcode
// Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
// Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
// Use two colors are enough but it needs a parent to tell not go back
bool validTree(int n, vector<pair<int, int>>& edges) {
    unordered_map<int, vector<int>> mp;
    for(auto e : edges){
        mp[e.first].push_back(e.second);
        mp[e.second].push_back(e.first);
    }
    vector<int> visited(n, 0);
    if(hasCycle(-1, 0, mp, visited)) return false;  // has cycle
    for(auto v : visited){
        if(v == 0) return false;  // not connected
    }
    return true;
}
bool hasCycle(int p, int i, unordered_map<int, vector<int>>& mp, vector<int>& visited){
    visited[i]=1;
    if(mp.find(i)!=mp.end()){
        for(auto k : mp[i]){
            if(k==p) continue;
            if(visited[k]==1) return true;
            if(visited[k]==0 && hasCycle(i, k,mp,visited)) return true;
        }
    }
    return false;
}
// using stack
bool hasCycle(int p, int i, unordered_map<int, vector<int>>& mp, vector<int>& visited){
    stack<pair<int,int>> st;
    st.push({p, i});
    while(!st.empty()){
        auto u = st.top();
        auto x = u.first;
        auto y = u.second;
        visited[y]=1;
        st.pop();
        if(mp.find(y)!=mp.end()){
            for(auto k : mp[y]){
                if(k == x) continue;
                if(visited[k]==1) return true;
                else st.push({y, k});
            }
        }
    }
    return false;
}
