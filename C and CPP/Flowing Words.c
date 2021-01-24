#include<stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include<string.h>
int main(){
    char inputSentence[100]={"\0"};
    char words[100][100]={"\0"};
    char first_str[2][100]={"\0"};
    char last_str[2][100]={"\0"};
    char* pFirst[2];
    char* pLast[2];
    int count=0;
    int group=0;
    char *p;
    char *q;
    gets(inputSentence);
    //Split input string to string array
    p=inputSentence;
    q=words[group];
    while (*p !='\0')
    {
        if (*p !=' '){
            *(q+count) =tolower(*p);
            count++;
        }else {
            q=words[++group];
            count=0;
        }
        *p++;
    }
    //Refresh string arrays
    count=0;
    pFirst[0]=first_str[0];
    pLast[0]=last_str[0];
    for (int i=0; i<10;i++){
        p = words[i];
        if (strlen(p)>0){
            *(pFirst[0]+count) =p[0];
            *(pLast[0]+count) =p[strlen(p)-1];
        }else {
            break;
        }
        count++;
    }
    //Obtain first and last chars of every string arrays
    pFirst[1]=first_str[1];
    pLast[1]=last_str[1];
    count=1;
    while(count<strlen(first_str[0])) {
        *(pFirst[1]+count-1) =*(pFirst[0]+count);
        count++;
    }
    count=0;
    while(count<strlen(last_str[0])-1){
        *(pLast[1]+count)=*(pLast[0]+count);
        count++;
    }
    //Show result
    printf("%s\n", (strcmp(first_str[1],last_str[1]) == 0)?"true":"false");
    return 0;
}

