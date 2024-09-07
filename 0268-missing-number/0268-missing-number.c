int missingNumber(int* nums, int numsSize) {
    int sum = 0;
    int n = 0;
    while(n <= numsSize){
        sum += n;
        n++;
    }
    for(int i=0; i<numsSize; i++){
        sum = sum - *(nums + i);
    }
    return sum;
}