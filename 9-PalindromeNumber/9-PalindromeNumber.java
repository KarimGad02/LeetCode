// Last updated: 24/11/2025, 17:27:29
class Solution {
    public boolean isPalindrome(int x) {
        
        boolean flag = false;
        String reversed = "";
        String number = String.valueOf(x);
        for(int i = 0; i<number.length(); i++){
            char RtoL = number.charAt(i);
            reversed = RtoL+reversed;
        }
        if(reversed.equals(number)){
        flag = true;
        }
        return flag;
    }
}