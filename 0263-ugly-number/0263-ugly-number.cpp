class Solution {
public:
    bool isUgly(int n) {
        int factors[] = {2,3,5};
        int i = 0;
        if(n <= 0) return false;
        while(i < 3){
            if(n % factors[i] == 0){
                n /= factors[i];
                i = -1;
            }
            i++;
        }
        return n==1;
    }
};