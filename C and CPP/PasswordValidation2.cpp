#include <iostream>
#include <string>

using namespace std;
int main() {
    const string NUMBERS= "0123456789";
    const string  SPECIALCHARS = "!@#$%&*";
    string words;
    int sum1=0;
    int sum2=0;
    cin>>words;
    for (char& c : words) {
        if (NUMBERS.find(c) != string::npos) {
            sum1++;
        };
        if (SPECIALCHARS.find(c) != string::npos) {
            sum2++;
        };
    }
    bool cond = (words.length()>=7) && (sum1 >=2) && (sum2 >=2); 
    string decide =cond? "Strong":"Weak";
    cout<<decide<<endl;
}