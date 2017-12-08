#include <iostream>
#include <string>
#include <algorithm>  //transform
#include <vector>
#include <numeric>    //accumulate
using namespace std;

int main(){
  int a = 123;
  string b = to_string(a); // "123"
  vector<char> c(b.begin(),b.end()); //{'1', '2', '3'}
  string d(c.begin(), c.end()); // "123"
  int e = stoi(d); // 123
  
  vector<int> v1 = {1,2,3,4};
  int f = accumulate(v1.begin(), v1.end(), 0); // 10
  int g = accumulate(v1.begin(), v1.end(), 0, [](int l, int r){return l*10+r;}); // 1234
  
  vector<char> v2 = {'1', '2', '3', '4'};
  string h(v2.begin(), v2.end());  // "1234"
  transform(v2.begin(), v2.end(), v2.begin(), [](char a){return (int)(a-'0');});
  int i = accumulate(v2.begin(), v2.end(), 0, [](int l, int r){return l*10+r;}); // 1234
  
  return 0;
}

