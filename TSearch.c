#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int ans(int v[], int s, int e, int z){
    int n = e-s;
    int t1 = s+(n/3);
    int t2 = s+(2*n/3);
    if(s==e){
        if (v[s] == z){
            return s;
        }else{
            return -1;
        }
    }else if(z > v[t1]){
        if(z>v[t2]){
            return ans(v, t2+1, e, z);
        }else{
            return ans(v, t1+1, t2, z);
        }
    }else{
        return ans(v, s, t1, z);
    }
}

int tsearch(int v[], int n, int z){
    return ans(v, 0, n-1, z);
}

int main(){
    int v[] = {1,2,3,4,5,6,7,8,9,10,11,12};
    int x;
    x = tsearch(v, 12, 5);
    printf("%d", x);
}