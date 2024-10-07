#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int arr[4] = {1,5,7,1};
    sort(arr,arr+4);
    for(int i = 0; i < 4; i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}