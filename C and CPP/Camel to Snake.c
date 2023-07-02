#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define UNDER  "_"
#define LENGTH 100
#define MIN1 65
#define MAX1 90
#define MIN2 97
#define MAX2 122

int main(){
    char str0[LENGTH];
    // printf("Input string: ");
    fgets(str0, LENGTH, stdin);
    char str[LENGTH]={};
    char *p1 = str0;
    char *p2 = str;
    char c;
    for (int i =0; i<strlen(str0)-1;i++){
        c= *(p1+i);
        if (c>=MIN1 && c <=MAX1)  //Capital letter
        {
            //Convert to small letter
            c += 32;
            if (i>0) //Not first letter
            {
                *p2++ = '_';
            };
        }
        *p2++=c;
    }
    printf("%s",str);
    return 0;
}