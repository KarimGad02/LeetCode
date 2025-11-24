// Last updated: 24/11/2025, 17:27:29
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        outerloop:
        for(int i = 0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(nums[i] + nums[j] == target && i != j){
                    result[0]=i;
                    result[1]=j;
                    break outerloop;
                }
            }
        }
        return result;
    }
}