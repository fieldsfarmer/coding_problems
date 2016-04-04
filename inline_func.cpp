#include <iostream>
#include <string>
using namespace std;

inline const string& shorterString(const string& s1, const string& s2){
	return s1.size() < s2.size()? s1 : s2;
}

int main(){
	string s1 = "hello, chicago!";
	string s2 = "hello, pittsburgh!";
	cout << shorterString(s1, s2) << endl;
	return 0;
}