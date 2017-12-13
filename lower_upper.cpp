#include <string>
#include <iostream>
#include <algorithm> // transform
using namespace std;
int main(){
  string a = "123abc";
  string c = "123ABC";
  transform(a.begin(), a.end(), a.begin(), ::toupper);
  transform(c.begin(), c.end(), c.begin(), ::tolower);
  cout << a << endl;
  cout << c << endl;
  char b = 'a';
  cout << char(::toupper(b)) << endl; // A if no char, then will print out 65
  
  return 0;
}
