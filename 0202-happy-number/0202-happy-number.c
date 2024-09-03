bool isHappy(int n) {
    int sum = 0;
    
    while(n>0){
        int num = n%10;
        sum += num*num;
        n = n/10;
    }
    n = sum;
    
    if(sum == 1){return 1;}
    else{
        while(n>0){
            sum = 0;
            while(n>0){
                int num = n%10;
                sum += num*num;
                n = n/10;
            }
            n = sum;
            if(n == 1){return 1;}
            else if(n==89){return 0;}          
        }
    }
    return 0;
}