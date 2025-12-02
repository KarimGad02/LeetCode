class Solution {
public:
    bool isUgly(int n) {
        int factors[] = {2,3,5};
        int i = 0;
        if(n <= 0) return false;
        if(n == 1) return true;
        while(i < 3){
            if(n % factors[i] == 0){
                n /= factors[i];
                i = -1;
            }
            if(n == 1) return true;
            i++;
        }
        return false;
    }
};