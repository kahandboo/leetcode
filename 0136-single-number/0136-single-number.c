int singleNumber(int* nums, int numsSize) {
    int count = 0; //
    if (numsSize == 1) return *nums;
    else{
        for(int i=0; i<numsSize; i++){
            int temp = *(nums+i);
            for(int j=0; j<numsSize; j++){
                if((temp != *(nums + j))){ 
                    count++;
                }
            }
            if(count == numsSize - 1){return temp;}
            count = 0;
        }
    }
    return 0;

}