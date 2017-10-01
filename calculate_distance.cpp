// Given a vector T of length N. T[i] denotes that i is connected to the neighbor T[i]. If i == T[i], it's the capital.
// The N nodes 0, ..., N-1 form a tree (i.e. all of them are connected and there is no loop).
// Return a vector S of length N-1. S[i] is the number of nodes that have distance of i+1 from the capital.
// For example, T[0]=9, T[1]=1, T[2]=4, T[3]=9, T[4]=0, T[5]=4, T[6]=8, T[8]=0, T[9]=1
// Then it will return [1,3,2,3,0,0,0,0,0] because 1 is the captial. 9 is distance 1 from it. [0,3,7] is distance 2 from it. [4,8] is distance 3 from it. [2,5,6] is distance 4 from it.
// The worst time complexity is required to be O(N). The worst space is also the same.
#include <vector>
#include <algorithm>
#include <stack>
#include <unordered_map>
#include <tuple>

vector<int> solution(vector<int> &T) {
    // write your code in C++14 (g++ 6.2.0)
    int len = T.size();
    if (len <= 1) return {};
    vector<int> res(len-1, 0);
    int capital = -1;
    unordered_map<int, vector<int>> d;
    for(auto i=0; i<len; ++i){
        if(T[i] != i)
            d[T[i]].push_back(i);
        else
            capital = i;
    }
    stack<tuple<int,int>> st;
    //In the following, I made a misktake
    //st.push(make_tuple(d[capital][0],1));
    //The following is right!
    for(auto i : d[capital])
        st.push(make_tuple(i,1));
    while(st.size()>0){
        auto u = st.top();
        st.pop();
        res[get<1>(u)-1] += 1;
        for(auto i : d[get<0>(u)])
            st.push(make_tuple(i, get<1>(u)+1));
    }
    return res;
}
