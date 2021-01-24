#include<iostream>
#include <string>
using namespace std;
int main() {
    string message,spyLife;
    getline(cin,message);
    for (char c : message){
        if (isalpha(c)|| c==' '){
            spyLife=c+spyLife;
        };
    }
    cout<<spyLife;
}