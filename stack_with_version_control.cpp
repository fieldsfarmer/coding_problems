// Implement a data structure which has the APIs of a stack.
// Moreover, it has three more APIs: 
// begin (which starts a new session); 
// rollback (which close all operations in the session if any un-committed operations and return true; otherwise, return false)
// commit (which commit the operations if there are un-commited ones; otherwise return false)
// The following code works in the test1, but still does not pass other tests (which I don't know what they are)

class Solution {
public:
    Solution() : v_(0), open_(false){}

    void push(int value) {
        st_.push(make_tuple(value, v_));
    }

    int top() {
        if(st_.empty()) return 0; // The return value is specified in the problem.
        return get<0>(st_.top());
    }

    void pop() {
        if(!st_.empty())
            st_.pop();
    }

    void begin() {
        v_+= 1;
        open_ = true;
    }

    bool rollback() {
        if(!open_ || v_ == 0) return false;
        while(!st_.empty() && get<1>(st_.top()) >= v_){
            st_.pop();
        }
        v_ -= 1;
        return true;
    }

    bool commit() {
        if(!open_ || v_ == 0) return false;
        open_ = true;
        v_-=1;
        return true;
    }
private:
  stack<tuple<int,int>> st_;
  int v_;
  bool open_;
};


void test() {
    Solution sol;
    sol.push(4);
    sol.begin();
    sol.push(7);                    // stack: [4,7]
    sol.begin();                    // start transaction 2
    sol.push(2);                    // stack: [4,7,2]
    assert(sol.rollback() == true); // rollback transaction 2
    assert(sol.top() == 7);         // stack: [4,7]

    sol.begin();                    // start transaction 3程序员野生保护区
    sol.push(10);                   // stack: [4,7,10]
    assert(sol.commit() == true);   // transaction 3 is committed
    assert(sol.top() == 10);
    assert(sol.rollback() == true); // rollback transaction 1
    assert(sol.top() == 4);         // stack: [4]
    assert(sol.commit() == false);
}
