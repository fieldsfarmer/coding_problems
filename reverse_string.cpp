#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

void reverseString(string& s){
	// string r = s;
	int l = s.size();
	if(l<2) return;
	reverse(s.begin(), s.end());
	// i is the first non-space position
	// j is the first space position after i
	int i=0, j=0;
	while(i<l){
		while(s[i]==' ') ++i;
		j = i;
		while(j<l && s[j]!=' ') ++j;
		reverse(s.begin()+i, s.begin()+j);
		i = j;
	}
}

int main(){
	string s = "hello   world  ";
	
	cout << s << endl;

	reverseString(s);
	
	cout << s << endl;
	
	return 0;
}