#include <iostream>
#include <deque>


int main(){

    using namespace std;

    deque<int> dq {1, 2, 3};

    dq.clear();

    cout << dq.size() << endl;
    // cout << dq.back() << endl;

    for(auto it = dq.cbegin(); it != dq.cend(); ++it)
        cout << *it << " ";

    cout << endl;

    return 0;
}