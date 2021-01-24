#include <iostream>
using namespace std;
int main(){
    const double TAX=0.07;
    const double DISCOUNT=0.1;
    const double PRICE=5.0;
    int amount;
    cin>>amount;
    double sum= amount * PRICE;
    if (amount >1 ) sum *= (1-DISCOUNT);
    sum *= (1+TAX);
    // cout<<sum<<endl;
    printf("%.2f",sum);
}