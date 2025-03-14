#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

float peaks(float v[], int s, int e){
    int m;
    m = (s+e)/2;
    if(s==e){
        return v[s];
    }if (v[m+1]>v[m]){
        return peaks(v, m+1, e);
    }else{
        return peaks(v, s, m);
    }
}

int main(){
    float v[] = {123,300,220,33,31,30,8,7,6,5,4,3,2};
    float x;
    x = peaks(v, 0, 11);
    printf("%f", x);
}