#include <stdio.h>
#include <stdlib.h>

void insertionSort(int arr[], int n){
    int i, key, j;
    for (i = 1; i < n; i++){
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key){
            arr[j + 1] = arr[j];
            j = j - 1;
        }arr[j + 1] = key;
    }
}

void insertionDecSort(int arr[], int n){
    int i, key, j;
    for (i = 1; i < n; i++){
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] < key){
            arr[j + 1] = arr[j];
            j = j - 1;
        }arr[j + 1] = key;
    }
}
void q4(int arr[], int n){
    int aeven[n/2];
    int aodd[n/2];
    int auxeven = 0, auxodd = 0;
    for(int i = 0; i < n; i++) {
        if (arr[i]%2 == 0){
            aeven[auxeven] = arr[i];
            auxeven++;
        }else{
            aodd[auxodd] = arr[i];
            auxodd++;
        }
    }insertionSort(aeven, (n/2));
    insertionDecSort(aodd, (n/2));
    auxeven = 0;
    auxodd = 0;
    for(int i = 0; i<n; i++){
        if (i%2 == 0){
            arr[i]=aeven[auxeven];
            auxeven++;
        }else{
            arr[i] = aodd[auxodd];
            auxodd++;
        }
        printf("%d > ", arr[i]);
    }
}

int main(){
    int v[] = {10, 1, 9, 7, 8, 2, 3, 6, 4, 5};
    q4(v, 10);
}
