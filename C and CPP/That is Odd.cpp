#include <iostream>
#include <vector>
// #include <algorithm> // use sort
using namespace std;
int main() {
    int num;
    int elem;
    cin>>num;
    vector<int> vc;
    for (int i=0;i<num;i++){
        cin>>elem;
        vc.push_back(elem);
    }
    // std::sort(vc.begin(),vc.end());
    elem=0;
    for (int i=0;i<vc.size();i++){
        if (vc.at(i) % 2 == 0){
            elem+=vc.at(i);
        }
    }
    cout<<elem<<endl;

}

