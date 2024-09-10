int minSubArrayLen(int target, int* nums, int numsSize) {
    int min_length = INT_MAX;
    int sum = 0;
    int left = 0;

    for(int right = 0; right<numsSize; right++){
        sum+=nums[right];

        while(sum>=target){
            min_length = right-left+1 < min_length ? right-left+1 : min_length;
            sum-=nums[left++];
        }
    }
    return min_length == INT_MAX ? 0:min_length;
}