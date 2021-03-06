#include <iostream>
#include <string>
#include <sstream> // istringstream
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
  string delimiter = " "; // it can be any size string
  while((next = a.find(delimiter, last))!=string::npos){
    auto t = a.substr(last, next-last);
    if(t.size() > 0) cout << t << endl;
    last = next+1;
  }
  auto t = a.substr(last);
  if(t.size() > 0) cout << t << endl;
  
  //Method 2, only works on char demiliter
  string b = "nihao\nshijie\n";
  string out;
  istringstream ss(b);
  while(getline(ss, out, '\n')){
    cout << out << endl;
  }
  return 0;  
}
