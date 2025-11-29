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