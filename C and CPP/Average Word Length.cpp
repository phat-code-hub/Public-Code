#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;
int main(){
    string words;
    getline(cin,words);
    char cs[100];
    strcpy(cs,words.c_str());
    vector<string> res;
    string str;
    for (char p:cs){
       if (p=='\0') {
           if (str!="") res.push_back(str);
           break;}
       if (p !=' '){
          str.append(1,p);
       }
       else {
           if (str!="") res.push_back(str);
           str="";
       }
    }
    int len=res.size();
    int lenstr=0;
    double ave=0.0;
    for (string st:res){
        lenstr += st.length();
    }
    ave=(double)lenstr / (double)len;
    if (ave >= 3.5) cout<<ceil(ave)<<endl;
    else cout<<round(ave)<<endl;
    return 0;
}   
