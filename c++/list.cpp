#include <iostream>
#include <list>



int main() {

    using namespace std;

    list<int> lst;

    lst.push_back(99);
    lst.push_front(44);
    lst.push_front(-99);
    lst.push_back(-4);

    for(auto it = lst.cbegin(); it != lst.cend(); ++it) {
       
        cout << *it << " ";
    }

    cout << endl;

    auto start_it = lst.cbegin();
    auto stop_it = lst.cend();

    lst.erase(++start_it, --stop_it);

    // if (!lst.empty()) {
    //     cout << lst.front() << endl;
    //     cout << lst.back() << endl;
    // }

    for(auto it = lst.cbegin(); it != lst.cend(); ++it) {
       
        cout << *it << " ";
    }

    cout << endl;


    return 0;
}