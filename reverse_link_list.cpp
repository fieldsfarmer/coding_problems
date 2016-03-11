#include <iostream>

using namespace std;

struct Node{
	int val;
	Node* next;
	Node(int x): val(x), next(NULL){}
};

// void reverseLinkList(Node* head){
// 	if(!head || !(head->next)) return;
// 	Node tmp = Node(0);
// 	Node* dummy = &tmp;
// 	dummy->next = head;
// 	Node* p = head;
// 	while(p->next){
// 		Node* t = p->next;
// 		p->next = t->next;
// 		t->next = dummy->next;
// 		dummy->next = t;
// 	}
// 	head = dummy->next;
// }

Node* reverseLinkList_1(Node* head){
	if(!head || !(head->next)) return head;
	Node dummy = Node(0);
	Node* pre = &dummy;
	pre->next = head;
	Node* cur = head;
	while(cur->next){
		Node* t = cur->next;
		cur->next = t->next;
		t->next = pre->next;
		pre->next = t;
	}
	return pre->next;
}

void print(Node* head){
	if(!head) return;
	Node* p = head;
	while(p){
		cout << p->val << " ";
		p = p->next;
	}
	cout << endl;
}
int main(){
	Node a = Node(1);
	Node b = Node(2);
	Node c = Node(3);
	a.next = &b;
	b.next = &c;
	
	Node* p = reverseLinkList_1(&a);
	print(p);
	return 0;
}