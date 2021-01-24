#include <stdio.h>
#include<stdbool.h>
#include <stdlib.h>
#include<string.h>
#include <ctype.h>
#define SPECIAL "!#$%&*"
int main(){
    char  words[100];
    gets(words);
    char *p ;
    char *ret;
    p=&words;
    int sum1=0, sum2 =0;
    while (*p !='\0'){
        ret=strchr(SPECIAL,*p);
        if (ret !=NULL) sum1++;
        if (isdigit(*p)) sum2++;
        p++;
    }
    bool ans = (strlen(words) >=7 && (sum1 >=2) && (sum2 =2)) ;
    printf ("%s\n",(ans ==1)?"Strong":"Weak");
    return 0;
}