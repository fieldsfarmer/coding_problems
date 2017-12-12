#include <iostream>
#include <string>
using namespace std;
int main(){
  string a = "hello word it's    me I   am 123";
  // we want to print out hello\nword\nit's\nme\nI\nam\n123\n
  int next = 0, last = 0;
  string delimiter = " ";
  while((next = a.find(delimiter, last))!=string::npos){
    auto t = a.substr(last, next-last);
    if(t.size() > 0) cout << t << endl;
    last = next+1;
  }
  auto t = a.substr(last);
  if(t.size() > 0) cout << t << endl;
  return 0;  
}
