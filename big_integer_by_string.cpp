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
	string trim(string s);
	string positive_add(string a, string b);
	string positive_substract(string a, string b);
	// a>b: 1; a==b: 0; a<b: -1
	int positive_compare(string a, string b);
public:
	BigInteger(){
		num = "0";
		neg = false;
	}
	BigInteger(string s);
	void print();
	BigInteger add(BigInteger b);
	BigInteger substract(BigInteger b);
};

int BigInteger::positive_compare(string a, string b){
	a = trim(a);
	b = trim(b);
	if(a==b) return 0;
	int asz = a.size(), bsz = b.size();
	if(asz == bsz){
		for(int i=0; i<asz; ++i){
			if(a[i] < b[i])
				return -1;
			else if(a[i] > b[i])
				return 1;
		}
		return 0;
	}
	else if(asz < bsz){
		return -1;
	}
	else{
		return 1;
	}
}

string BigInteger::trim(string s){
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

string BigInteger::positive_substract(string a, string b){
	a = trim(a);
	b = trim(b);
	string s = a;
	if(positive_compare(a, b) == 0) 
		return "0";
	else if(positive_compare(a, b) > 0){
		int asz = a.size(), bsz = b.size();
		int diff = (int)(asz - bsz);
		b.insert(0, diff, '0');
		for(int i=asz-1; i>=0; --i){
			if(a[i] < b[i]){
				a[i]+=10;
				a[i-1]-=1;
			}
			s[i] = (a[i]-'0')-(b[i]-'0')+'0';
		}
		s = trim(s);
	}
	return s;
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

BigInteger BigInteger::substract(BigInteger b){
	return BigInteger(positive_substract(this->num, b.num));
}

int main(){
	BigInteger s("000123");
	BigInteger t("03210");
	BigInteger res = s.add(t);
	res.print();
	BigInteger res1 = t.substract(s);
	res1.print();
	return 0;
}