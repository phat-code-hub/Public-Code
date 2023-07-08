/*
    Input : A string contain multiples words
    output: A number represent the average length of each word, rounded up to nearest whole number 
            (space and punctuations are not count )
    Example :"This phrase has multiple words!!"
            -> 6
        It has total 26 letters and 5 words  -> average is 5.2 -> round to 6 
    Made  by Ueda July 2023
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define SPACE ' '
#define LENGTH 200
#define MIN1 65
#define MAX1 90
#define MIN2 97
#define MAX2 122

int main(){
    char str[LENGTH]={};
    char res[LENGTH] ={};
    printf("Input string: ");
    fgets(str, LENGTH, stdin);
    char *p = str ;
    char *r = res;
    int words = 0;
    int avg;
    while(*p != '\0'){
        if (*p != SPACE) {
            if((*p >= MIN1 && *p<=MAX1) || (*p>=MIN2 && *p<=MAX2)) *r++ = *p;
        } else words++;
        *p++;
    }
    int len = strlen(res);
    float avg_f = (float) len /(words+1);
    avg=ceil(avg_f);
    printf("average is:%d", avg);
    return 0;
}