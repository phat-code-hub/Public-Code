#include<stdio.h>
#define PRICE  3000000
#define INSURANCE  1000000
#define MONTHLY_CAPACITY 10
#define UNIT_COST 2000000
int main(){
    int monthly_cost = UNIT_COST * MONTHLY_CAPACITY+ INSURANCE;
    int customer =0;
    scanf("%d",&customer);
    int income = PRICE * customer;
    if(income > monthly_cost ) printf("Profit");
    else if ( income == monthly_cost) printf("Broke Even");
    else printf("Loss");
    return 0;
}