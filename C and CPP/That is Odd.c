#include<stdio.h>
#include <stdlib.h>
int main(){
    int num;
    scanf("%d",&num);
    int sum=0;
    int n;
    for (int i=0;i<num;i++){
        scanf("%d",&n);
        if (n %2 == 0) sum += n;    
    }
    printf("%d",sum);
    return 0;
}