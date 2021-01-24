#include<iostream>
#include <string>
#include <regex>
using namespace std;
int main()
{
    string words;
    getline(cin,words);
    regex reg("\\$(x)*T|T(x)*\\$",regex::extended);
    if (regex_search(words,reg)) cout<<"ALARM"<<endl;
    else cout<<"quiet"<<endl;
    return 0;
}