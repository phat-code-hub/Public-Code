#include<iostream>
#include <string>
using namespace std;
int main(){
    string words;
    getline (cin,words);
    string  word[12];
    int limits=0;
    for (auto &&wd : words)
    {
        if (wd!=' '){
            word[limits].push_back(wd);
        } else{
            if (wd == '\0'){
                break;
            }
            limits++;
        }
    }
    string pigLatin="";
    for (int z =0; z<=limits;z++){
        word[z].push_back(word[z][0]);
        word[z].erase(0,1);
        word[z]+="ay ";
        pigLatin+=word[z];
    }
    pigLatin.erase(pigLatin.size()-1,1);
    cout<<pigLatin<<endl;
}