//map example: http://www.cplusplus.com/reference/map/map/lower_bound/
//set example: http://www.cplusplus.com/reference/set/set/lower_bound/

#include <iostream>
#include <set>
using namespace std;
int main() {
  set<int> s;
  s.insert(10); s.insert(20); s.insert(30);
  cout << *(s.lower_bound(10)) << endl; //10
  cout << *(s.upper_bound(10)) << endl; //20
  return 0;
}

// https://leetcode.com/problems/contains-duplicate-iii/description/

