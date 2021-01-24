#include <iostream>
#include <string>
#include <vector>
using namespace std;
//-----------------------------------------------------
vector<string> split(string st){
    vector<string> res;
    string temp;
    string *p=&st;
    for (auto c:*p){
        if (c != ' ') {
           temp +=c;
        } else {
             res.push_back(temp);
             temp="";
        }
    }
    res.push_back(temp);
    return res;
}
//-----------------------------------------------------
int main (){
    vector<string> words;
    string wd;
    string first_char="";
    string last_char="";
    getline(cin,wd);
    words=split(wd);
    for(auto  s:words){
        first_char +=s[0];
        last_char +=s[s.length()-1];
    }
    first_char=first_char.substr(1);
    last_char=last_char.substr(0,last_char.length()-1);
    string ans=(first_char == last_char)?"true":"false";
    cout<<ans<<endl;
    return 0;
}