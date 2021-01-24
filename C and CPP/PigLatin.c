#include <stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
    char wd[5];
    char abc[5][5];
    char cuoi[5];
    gets(wd);
    char *p=wd;
    // char *q=abc;
    int cnt=0;
    int y=0;
    for (int i=0;i<strlen(wd);i++){
        // printf("%c",*(p+i));
        // q=p+i;
        // abc[i]=*q;
        if (*(p+i) != ' '){
            abc[cnt][y++] =*(p+i);
        } else {
            // for (int z=0; z<=y;z++){
            //     printf("%c",abc[cnt][z]);
            // };
            cnt++;
            y=0;
        };
    //    for (int i =0; i<=cnt;i++){
    //        printf("%s",abc[i]);
    //        printf("");
    //    }
        
        // printf("%s",abc[1]);
    };
    printf("%s\n",abc[0]);
    printf("%s\n",abc[1]);
    return 0;
}