#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>
using namespace std;

void count_char(string str){
    unordered_map<char, int> mp;
    for(auto c : str){
        mp[c]++;
    }
    vector<pair<char, int>> v(mp.begin(), mp.end());
    sort(v.begin(), v.end(), [](const pair<char,int>& a, const pair<char, int>& b){return a.second>b.second;});
    for(auto itr : v){
        cout << itr.first << " " << itr.second << endl;
    }
}

template<typename T> void print_pq(T& pq){
    while(!pq.empty()){
        cout << pq.top().first << " " << pq.top().second << endl;
        pq.pop();
    }
}

void top_char(string str, int k){
    unordered_map<char,int> mp;
    for(auto c : str) mp[c]++;
    auto cmp=[](pair<char,int>& a, pair<char,int>& b) {return a.second > b.second;};
    priority_queue<pair<char, int>, vector<pair<char, int>>, decltype(cmp)> pq(cmp);
    int cnt = 0;
    for(auto itr : mp){
//         if(cnt < k){
//             pq.push(itr);
//             cnt ++;
//         } else {
//             if(itr.second > pq.top().second){
//                 pq.pop();
//                 pq.push(itr);
//             }
//         }
        pq.push(itr);
        if(pq.size() > k) pq.pop();
    }
    print_pq(pq);
}

int main() {
    string s = "nimanibanidienimei";
    count_char(s);
    cout << "=============" << endl;
    top_char(s, 2);
    return 0;
}
