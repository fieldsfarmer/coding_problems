#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// tail recursion
bool helper(bool isEdited, string s, int m, string t, int n){
	if(m>=s.size()){
		if(n>=t.size()) return isEdited;
		else return (n+1==t.size() && !isEdited);
	}
	if(n>=t.size()){
		if(m>=s.size()) return isEdited;
		else return (m+1==s.size() && !isEdited);
	}
	if(s[m] == t[n]){
		return helper(isEdited, s, m+1, t, n+1);
	}
	else{
		if(isEdited) return false;
		return helper(true, s, m+1, t, n) || helper(true, s, m, t, n+1) || helper(true, s, m+1, t, n+1);
	}
}

bool isOneEditDistance(string s, string t){
	if(s.empty() && t.empty()) return false;
	if(abs((int)(s.size() - t.size())) > 1) return false;
	return helper(false, s, 0, t, 0);
}

bool isOneEditDistance_1(string s, string t){
	int ssz = s.size();
	int tsz = t.size();
	if(ssz > tsz) return isOneEditDistance(t, s);
	if(tsz-ssz>1) return false;
	bool flag = false;
	for(int i=0, j=0; i<ssz; ++i, ++j){
		if(s[i] != t[j]){
			if(flag) return false;
			flag = true;
			if(ssz < tsz) --i;
		}
	}
	return flag || (ssz < tsz);
}
int main(){
	// string s = "ac";
	// string t = "ab"; // they should be one distance
	string s = "ac";
	string t = "abc";
	// if(isOneEditDistance(s, t))
	if(isOneEditDistance_1(s, t))
		cout << "They are one edit distance!" << endl;
	else
		cout << "No!" << endl;
	return 0;
}