// Big integer with add

#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

class BigInteger{
private:
	string num;
	bool neg;
	string positive_add(string a, string b);
public:
	BigInteger(){
		num = "0";
		neg = false;
	}
	BigInteger(string s);
	void print();
	BigInteger add(BigInteger b);
};

string trim(string s){
	if(s.size()<=1) return s;
	int position = 0;
	for(int i=0; i<s.size(); ++i){
		if(s[i]=='0'){
			position++;
		}
		else
			break;
	}
	return s.substr(position);
}

string BigInteger::positive_add(string a, string b){
	int carry = 0;
	a = trim(a);
	b = trim(b);
	if(a=="0" || a=="") return b;
	if(b=="0" || b=="") return a;
	int asz = a.size(), bsz = b.size();
	string add = (asz > bsz)? a : b;
	int diff = abs((int)(a.size() - b.size()));
	if(diff>0){
		if(asz > bsz){
			b.insert(0, diff, '0');
		}
		else if(asz < bsz){
			a.insert(0, diff, '0');
		}
	}
	for(int i=add.size()-1; i>=0; --i){
		add[i] = carry + (a[i]-'0') + (b[i]-'0') + '0';
		if(i!=0){
			if(add[i]-'0'>9){
				add[i] = add[i]-'0'-10+'0';
				carry = 1;
			}
			else
				carry = 0;
		}
	}
	if(add[0]-'0'>9){
		add[0] = add[0]-'0'-10+'0';
		add.insert(0,1,'1');
	}
	return add;
}

BigInteger::BigInteger(string s){
	if(isdigit(s[0])){
		num = s;
		neg = false;
	}
	else{
		num = s.substr(1);
		if(num.size()==0) num = "0";
		if(num!="0" && s[0]=='-')
			neg = true;
		else
			neg = false;
	}
}
void BigInteger::print(){
	if(neg){
		cout << "-" << num << endl;
	}
	else{
		cout << num << endl;
	}
}
BigInteger BigInteger::add(BigInteger b){
	return BigInteger(positive_add(this->num, b.num));
}

int main(){
	BigInteger s("000123000");
	BigInteger t("0321");
	BigInteger res = s.add(t);
	res.print();
	return 0;
}