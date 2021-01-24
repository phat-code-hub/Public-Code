#include <stdio.h>
#define TAX 0.07
#define DISCOUNT 0.1
#define PRICE 5.0
int main(){
    int amount=4;
    double sum;
    // scanf("%d",&amount);
    sum= (double) amount * PRICE;
    if (amount >1 ) sum *=(1-DISCOUNT);
    sum *= (1+TAX);
    printf("%.2f",sum);
}
