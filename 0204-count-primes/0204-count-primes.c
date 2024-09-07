int countPrimes(int n) {
    int *arr;
    int count = 0;
    arr = (int*) malloc((n+1) * sizeof(int)); 
    for(int i=1; i<n+1; i++){
        arr[i] = i;
    }
    for(int i=2; i<n+1; i++){
        if(arr[i] == 0) continue;
        else{
            int j=2;
            while(i*j <= n){
                arr[i*j] = 0;
                j++;
            }
        }
    }
    for(int i=2; i<n; i++){
        if(arr[i]==0) continue;
        else{
            count++;
        }
    }

    free(arr);
    return count;
}