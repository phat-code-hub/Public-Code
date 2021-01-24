#include<iostream>
#include <sstream>
using namespace std;
char toHex(int dec)
{
    std::stringstream a;
    a << std::hex << dec;
    return  a.str().c_str()[0];
}
int main() {
    int x;
    cin>>x;
    cout<<toHex(x)<<endl;

}

