#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;
void dfs(vector<int>& dic, vector<vector<int> >& res, vector<int>& tmp, int n);

vector<vector<int> > permutation(int n){
	vector<vector<int> > res;
	if(n<=0) return res;
	vector<int> dic(n, -1);
	vector<int> tmp;
	dfs(dic, res, tmp, n);
	return res;
}
// dfs recursive
void dfs(vector<int>& dic, vector<vector<int> >& res, vector<int>& tmp, int n){
	if(tmp.size()==n){
		res.push_back(tmp);
		return;
	}
	for(int i=0; i<n; ++i){
		if(dic[i]<0){
			dic[i]=1;
			tmp.push_back(i);
			dfs(dic, res, tmp, n);
			tmp.pop_back();
			dic[i]=-1;
		}
	}
}

// for ierative method, not easy using C++, better using python; see permutation.py
void print(vector<vector<int> > res){
	for(int i=0; i<res.size(); ++i){
		for(int j=0; j<res[i].size(); ++j){
			cout << res[i][j] << " ";
		}
		cout << endl;
	}
}
int main(){
	auto res = permutation(3);
	print(res);
}