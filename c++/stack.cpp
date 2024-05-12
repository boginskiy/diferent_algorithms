#include <iostream>
#include <stack>
#include <vector>
#include <list>


int main() {

    using namespace std;

    stack<int> st;


    st.push(1);
    st.push(2);
    st.push(3);

    while(!st.empty()) {
        cout << st.top() << endl;
        st.pop();
    }

    return 0;
}