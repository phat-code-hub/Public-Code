#include <iostream>
using namespace std;
int main(){
    string name,revName="";
    cin>>name;
    for (char c:name){
        revName = c+revName;
    }
    cout<<revName<<endl;
    return 0;
}