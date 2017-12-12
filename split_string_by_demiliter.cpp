#include <iostream>
#include <string>
using namespace std;
//https://stackoverflow.com/questions/14265581/parse-split-a-string-in-c-using-string-delimiter-standard-c
int main(){
  string a = "hello word it's    me";
  // we want to print out 
  //hello
  //word
  //it's
  //me
  
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
