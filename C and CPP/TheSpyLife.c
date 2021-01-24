#include <stdio.h>
#include<ctype.h>
#include <string.h>
#define MAX_LIMITS 100

int main(){
    char mess[MAX_LIMITS];
    char spyLife[MAX_LIMITS];
    char cuoi[MAX_LIMITS];
    fgets(mess,MAX_LIMITS,stdin);
    char* p = &mess;
    char* q = &spyLife;
    q=&spyLife;
    while (*p != '\0'){
        if ((isalpha(*p)) || *p == ' '){
            *q = *p;
            if (*p == ' '){
                strcat(spyLife,"ay");
            };
            q++;
        }
        p++;  
    }
    // printf("=>  %s",spyLife);
    printf("==> %s\n",cuoi);
    return 0;
}