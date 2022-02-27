#include<stdio.h>
#include <string.h>
#include<stdlib.h>
int main(){
    char str[100]="";
    char rev[100]="";
    scanf("%[^\n]",str);
    char *p,*q;
    p=&str[strlen(str)-1];
    q =(char *) malloc(strlen(str)*sizeof(char));
    q=&rev[0];
    int i=0;
    while (i<strlen(str)){
        *q=*(p-i++);
        q++;
    }
    printf("%s",rev);
    return 0;
}